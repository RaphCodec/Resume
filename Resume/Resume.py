"""Raphael Clifton - Data Engineer Resume"""

import reflex as rx
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def calc_exp(start: str, end: str = None, fmt: str = "%Y-%m-%d") -> str:
    """Calculate experience duration between two dates"""
    start_date = datetime.strptime(start, fmt)
    end_date = datetime.strptime(end, fmt) if end else datetime.combine(date.today(), datetime.min.time())
    diff = relativedelta(end_date, start_date)
    
    start_formatted = start_date.strftime("%b %Y")
    end_formatted = "Present" if (not end or end_date.date() == date.today()) else end_date.strftime("%b %Y")
    
    parts = []
    if diff.years:
        parts.append(f"{diff.years} yr" + ("s" if diff.years > 1 else ""))
    if diff.months:
        parts.append(f"{diff.months} mo" + ("s" if diff.months > 1 else ""))
    
    exp = " ".join(parts) if parts else "0 mos"
    return f"{start_formatted} - {end_formatted} · {exp}"


def navbar() -> rx.Component:
    """Navigation bar"""
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading("Raphael Clifton", size="6"),
                rx.text("Data Engineer", size="2", color="gray"),
                spacing="1",
                align_items="start",
            ),
            rx.spacer(),
            rx.hstack(
                rx.link("Experience", href="#experience"),
                rx.link("Education", href="#education"),
                rx.link("Skills", href="#skills"),
                spacing="5",
            ),
            rx.color_mode.button(),
            width="100%",
            max_width="1400px",
            padding="1rem 2rem",
            align="center",
            margin="0 auto",
        ),
        border_bottom="1px solid var(--gray-5)",
        bg="var(--color-surface)",
        width="100%",
    )


def hero() -> rx.Component:
    """Hero section"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Hello, World!",
                size="9",
                font_family="'Brush Script MT', cursive",
            ),
            rx.text(
                "👋🏽 My name is Raphael. I'm a Data Engineer and tech enthusiast.",
                size="5",
                text_align="center",
            ),
            rx.text(
                "Building reliable, scalable data systems that power business decisions.",
                size="4",
                color="white",
                text_align="center",
            ),
            rx.hstack(
                rx.link(
                    rx.button("View Experience", size="3"),
                    href="#experience",
                ),
                rx.link(
                    rx.icon_button(
                        rx.icon("github", size=20),
                        size="3",
                        variant="solid",
                        color_scheme="gray",
                    ),
                    href="https://github.com/RaphCodec",
                    is_external=True,
                ),
                rx.link(
                    rx.icon_button(
                        rx.icon("linkedin", size=20),
                        size="3",
                        variant="solid",
                        color_scheme="gray",
                    ),
                    href="https://www.linkedin.com/in/raphael-clifton/",
                    is_external=True,
                ),
                spacing="3",
            ),
            spacing="5",
            align="center",
            padding="6rem 2rem",
            width="100%",
        ),
        background="linear-gradient(135deg, var(--purple-9) 0%, var(--violet-9) 100%)",
        color="white",
        width="100%",
    )


def experience_card(role: str, company: str, period: str, bullets: list[str], skills: list[str]) -> rx.Component:
    """Individual experience card"""
    return rx.card(
        rx.vstack(
            rx.heading(role, size="5"),
            rx.text(company, color="gray", weight="medium"),
            rx.text(period, size="2", color="gray"),
            rx.divider(),
            rx.unordered_list(
                *[rx.list_item(bullet) for bullet in bullets],
                spacing="2",
            ),
            rx.hstack(
                *[rx.badge(skill, color_scheme="purple", variant="soft") for skill in skills],
                spacing="2",
                wrap="wrap",
            ),
            spacing="3",
            align_items="start",
        ),
    )


def experience_section() -> rx.Component:
    """Experience section with cards"""
    return rx.box(
        rx.vstack(
            rx.heading("Work Experience", size="8", id="experience"),
            rx.grid(
                experience_card(
                    "Deputy Director of Data Engineering and DevOps",
                    "New York City Department of Transportation",
                    calc_exp("2026-01-01", date.today().strftime("%Y-%m-%d")),
                    [
                        "Manage a team of data engineers and DevOps professionals",
                        "Implement and migrate data pipelines to Apache Airflow hosted on Azure AKS",
                        "Migrate analytics workloads to Snowflake from SQL Server",
                        "Develop DevOps CI/CD pipelines using GitHub Actions",
                        "Leverage GitHub Projects for task management and sprint planning",
                    ],
                    ["Python", "Airflow", "Azure", "Snowflake", "FastAPI"],
                ),
                experience_card(
                    "Data Engineer",
                    "New York City Department of Transportation",
                    calc_exp("2023-07-01", "2026-01-01"),
                    [
                        "Create and manage databases for analytics and web development",
                        "Create and maintain various data pipelines using Python and SQL",
                        "Built interactive Org Chart application for workforce planning",
                        "Contributed to Power BI dashboards for 311, Congestion Pricing, and KPIs",
                    ],
                    ["Python", "Airflow", "Azure", "Snowflake", "FastAPI"],
                ),
                experience_card(
                    "Data Engineering Intern | College Aide",
                    "New York City Department of Transportation",
                    calc_exp("2022-07-01", "2023-07-01"),
                    [
                        "Developed Python data pipelines for the central data unit",
                        "Reduced pipeline load times by 50-95%",
                        "Improved data quality and ETL reliability",
                    ],
                    ["Python", "SQL"],
                ),
                experience_card(
                    "Tutor",
                    "CUNY Tutor Corps",
                    calc_exp("2019-10-01", "2021-06-01"),
                    [
                        "Conducted group and one-on-one tutoring sessions remotely and in-person",
                        "Helped students develop mathematical and critical thinking skills",
                    ],
                    ["Communication", "Teaching"],
                ),
                experience_card(
                    "Operations Intern",
                    "CUNY Summer Corps",
                    calc_exp("2019-07-01", "2019-08-31"),
                    [
                        "Restocked and fixed printers daily",
                        "Assembled books for events as needed",
                        "Sorted and organized incoming and outgoing mail 3-4 times daily",
                    ],
                    ["Operations", "Organization"],
                ),
                experience_card(
                    "Front Desk Attendant",
                    "Baruch College (Economics and Finance Department)",
                    calc_exp("2018-10-01", "2019-05-31"),
                    [
                        "Answered student questions in person and on the phone",
                        "Restocked office supplies 2-3 times a day",
                    ],
                    ["Customer Service", "Administration"],
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="6",
            align="center",
            padding="4rem 2rem",
            max_width="1400px",
            width="100%",
            margin="0 auto",
        ),
        width="100%",
    )


def education_section() -> rx.Component:
    """Education section"""
    return rx.box(
        rx.vstack(
            rx.heading("Education", size="8", id="education"),
            rx.grid(
                rx.card(
                    rx.vstack(
                        rx.heading("Master's Degree", size="5"),
                        rx.text("CUNY Baruch College: Zicklin School of Business", weight="medium"),
                        rx.text("MS, Information Systems — Data Analytics", color="gray"),
                        rx.text("Jan 2022 - Jun 2023", size="2", color="gray"),
                        spacing="2",
                        align_items="start",
                    ),
                ),
                rx.card(
                    rx.vstack(
                        rx.heading("Bachelor's Degree", size="5"),
                        rx.text("CUNY Baruch College: Zicklin School of Business", weight="medium"),
                        rx.text("BBA, Economics", color="gray"),
                        rx.text("Sep 2017 - Jun 2021", size="2", color="gray"),
                        spacing="2",
                        align_items="start",
                    ),
                ),
                columns="2",
                spacing="4",
                width="100%",
            ),
            spacing="6",
            align="center",
            padding="4rem 2rem",
            max_width="1400px",
            width="100%",
            margin="0 auto",
        ),
        bg="var(--gray-2)",
        width="100%",
    )


def skills_section() -> rx.Component:
    """Skills section with categories"""
    skills_data = {
        "Programming": ["Python", "C#", "SQL"],
        "Orchestration & ETL": ["Apache Airflow", "Azure Data Factory"],
        "Data Warehousing": ["Snowflake", "SQL Server", "DuckDB", "Postgres"],
        "Backend": ["FastAPI", "Django"],
        "Frontend": ["React", "Reflex"],
        "Version Control": ["GitHub", "GitHub Actions", "Azure DevOps"],
    }
    
    return rx.box(
        rx.vstack(
            rx.heading("Skills", size="8", id="skills"),
            rx.grid(
                *[
                    rx.card(
                        rx.vstack(
                            rx.heading(category, size="4"),
                            rx.hstack(
                                *[rx.badge(skill, variant="soft") for skill in skills],
                                spacing="2",
                                wrap="wrap",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    )
                    for category, skills in skills_data.items()
                ],
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="6",
            align="center",
            padding="4rem 2rem",
            max_width="1400px",
            width="100%",
            margin="0 auto",
        ),
        width="100%",
    )


def footer() -> rx.Component:
    """Footer section"""
    return rx.box(
        rx.text(
            "© 2026 Raphael Clifton - Data Engineer",
            size="2",
            color="gray",
            text_align="center",
        ),
        padding="2rem",
        width="100%",
    )


def index() -> rx.Component:
    """Main page"""
    return rx.vstack(
        navbar(),
        hero(),
        experience_section(),
        education_section(),
        skills_section(),
        footer(),
        spacing="0",
        width="100%",
    )


app = rx.App()
app.add_page(index, title="Raphael Clifton - Resume")
