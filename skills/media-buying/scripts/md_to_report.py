#!/usr/bin/env python3
"""
Convert agent-produced markdown reports to styled HTML.
Detects report type (audit/plan/diagnosis) and applies appropriate styling.

Usage:
    python md_to_report.py <input.md> [--type audit|plan|diagnosis] [--open]
"""

import re
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

# Report type configurations
REPORT_TYPES = {
    "audit": {
        "color": "#DC2626",
        "title": "Media Audit Report",
    },
    "plan": {
        "color": "#003D5C",
        "title": "Campaign Plan",
    },
    "diagnosis": {
        "color": "#D97706",
        "title": "Performance Diagnosis",
    },
}

DETECTION_PATTERNS = {
    "audit": [r"P0\s*[—–-]\s*Critical", r"Audit Summary"],
    "plan": [r"Strategy Overview", r"Channel Mix"],
    "diagnosis": [r"Root Cause", r"Performance Diagnosis"],
}


def detect_type(content: str) -> str:
    for report_type, patterns in DETECTION_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return report_type
    return "plan"


def extract_metadata(content: str) -> dict:
    meta = {"title": "", "platform": "", "date": datetime.now().strftime("%B %d, %Y")}

    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        meta["title"] = title_match.group(1).strip()

    platform_match = re.search(
        r"\*\*Platform(?:\(s\))?\*?\*?:\s*\*?\*?\s*(.+?)$", content, re.MULTILINE
    )
    if platform_match:
        meta["platform"] = platform_match.group(1).strip().rstrip("*")

    date_match = re.search(r"\*\*Date\*?\*?:\s*\*?\*?\s*(.+?)$", content, re.MULTILINE)
    if date_match:
        meta["date"] = date_match.group(1).strip().rstrip("*")

    return meta


def extract_status(content: str, report_type: str) -> str:
    if report_type == "audit":
        health_match = re.search(
            r"\*\*Overall Health\*?\*?:\s*\*?\*?\s*(.+?)$", content, re.MULTILINE
        )
        if health_match:
            health = health_match.group(1).strip().rstrip("*")
            if "critical" in health.lower():
                return f'<div class="status-badge status-critical">{health}</div>'
            elif "needs" in health.lower() or "warning" in health.lower():
                return f'<div class="status-badge status-warning">{health}</div>'
            else:
                return f'<div class="status-badge status-healthy">{health}</div>'
    elif report_type == "diagnosis":
        severity_match = re.search(
            r"\*\*Severity\*?\*?:\s*\*?\*?\s*(.+?)$", content, re.MULTILINE
        )
        if severity_match:
            severity = severity_match.group(1).strip().rstrip("*")
            if "critical" in severity.lower():
                return f'<div class="status-badge status-critical">{severity}</div>'
            elif "high" in severity.lower():
                return f'<div class="status-badge status-warning">{severity}</div>'
            elif "moderate" in severity.lower():
                return f'<div class="status-badge status-info">{severity}</div>'
            else:
                return f'<div class="status-badge status-healthy">{severity}</div>'
    return ""


def convert_markdown_to_html(md: str) -> str:
    lines = md.strip().split("\n")
    html_lines = []
    in_table = False
    in_list = False
    in_ordered_list = False
    row_index = 0

    for line in lines:
        stripped = line.strip()

        # Skip the main title (already in header)
        if stripped.startswith("# ") and not stripped.startswith("## "):
            continue

        # Horizontal rule
        if re.match(r"^-{3,}$", stripped):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if in_ordered_list:
                html_lines.append("</ol>")
                in_ordered_list = False
            html_lines.append("<hr>")
            continue

        # Table rows
        if "|" in stripped and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if all(re.match(r"^[-:]+$", c) for c in cells):
                continue
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if not in_table:
                in_table = True
                row_index = 0
                html_lines.append("<table>")
            cells_html = [_inline(c) for c in cells]
            if row_index == 0:
                html_lines.append(
                    "<tr>" + "".join(f"<th>{c}</th>" for c in cells_html) + "</tr>"
                )
            else:
                html_lines.append(
                    "<tr>" + "".join(f"<td>{c}</td>" for c in cells_html) + "</tr>"
                )
            row_index += 1
            continue
        else:
            if in_table:
                html_lines.append("</table>")
                in_table = False
                row_index = 0

        # Headings
        h_match = re.match(r"^(#{2,4})\s+(.+)$", stripped)
        if h_match:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if in_ordered_list:
                html_lines.append("</ol>")
                in_ordered_list = False
            level = len(h_match.group(1))
            html_lines.append(f"<h{level}>{_inline(h_match.group(2))}</h{level}>")
            continue

        # Checklist items
        checklist_match = re.match(r"^-\s*\[([ xX])\]\s+(.+)$", stripped)
        if checklist_match:
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            done = checklist_match.group(1).lower() == "x"
            cls = "checklist-item checklist-done" if done else "checklist-item"
            html_lines.append(
                f'<li class="{cls}">{_inline(checklist_match.group(2))}</li>'
            )
            continue

        # Unordered list items
        ul_match = re.match(r"^(\s*)-\s+(.+)$", stripped)
        if ul_match:
            if in_ordered_list:
                html_lines.append("</ol>")
                in_ordered_list = False
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{_inline(ul_match.group(2))}</li>")
            continue

        # Ordered list items
        ol_match = re.match(r"^(\s*)\d+\.\s+(.+)$", stripped)
        if ol_match:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if not in_ordered_list:
                html_lines.append("<ol>")
                in_ordered_list = True
            html_lines.append(f"<li>{_inline(ol_match.group(2))}</li>")
            continue

        # Close open lists on non-list content
        if in_list and stripped:
            html_lines.append("</ul>")
            in_list = False
        if in_ordered_list and stripped:
            html_lines.append("</ol>")
            in_ordered_list = False

        # Empty line
        if not stripped:
            continue

        # Paragraph
        html_lines.append(f"<p>{_inline(stripped)}</p>")

    # Close any open elements
    if in_table:
        html_lines.append("</table>")
    if in_list:
        html_lines.append("</ul>")
    if in_ordered_list:
        html_lines.append("</ol>")

    return "\n".join(html_lines)


def _inline(text: str) -> str:
    # Severity badges
    text = re.sub(
        r"\bP0\b", '<span class="badge badge-p0">P0</span>', text
    )
    text = re.sub(
        r"\bP1\b", '<span class="badge badge-p1">P1</span>', text
    )
    text = re.sub(
        r"\bP2\b", '<span class="badge badge-p2">P2</span>', text
    )
    text = re.sub(
        r"\bP3\b", '<span class="badge badge-p3">P3</span>', text
    )
    # Severity word badges
    for word, cls in [
        ("Critical", "badge-critical"),
        ("High", "badge-high"),
        ("Moderate", "badge-moderate"),
        ("Low", "badge-low"),
    ]:
        text = re.sub(
            rf"\[{word}\]",
            f'<span class="badge {cls}">{word}</span>',
            text,
        )
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)

    input_path = Path(args[0])
    if not input_path.exists():
        print(f"Error: {input_path} not found")
        sys.exit(1)

    report_type = None
    open_browser = False
    for arg in args[1:]:
        if arg == "--open":
            open_browser = True
        elif arg == "--type":
            pass
        elif arg in ("audit", "plan", "diagnosis"):
            report_type = arg

    content = input_path.read_text(encoding="utf-8")

    if not report_type:
        report_type = detect_type(content)

    config = REPORT_TYPES[report_type]
    meta = extract_metadata(content)
    status_badge = extract_status(content, report_type)
    body_html = convert_markdown_to_html(content)

    template_path = Path(__file__).parent.parent / "templates" / "report-template.html"
    template = template_path.read_text(encoding="utf-8")

    subtitle = meta["title"] if meta["title"] != config["title"] else ""

    html = template.replace("{{REPORT_TITLE}}", config["title"])
    html = html.replace("{{SUBTITLE}}", subtitle)
    html = html.replace("{{DATE}}", meta["date"])
    html = html.replace("{{PLATFORM}}", meta["platform"])
    html = html.replace("{{TYPE_COLOR}}", config["color"])
    html = html.replace("{{STATUS_BADGE}}", status_badge)
    html = html.replace("{{CONTENT}}", body_html)

    output_path = input_path.with_suffix(".html")
    output_path.write_text(html, encoding="utf-8")
    print(f"Report generated: {output_path}")

    if open_browser:
        webbrowser.open(str(output_path.resolve()))


if __name__ == "__main__":
    main()
