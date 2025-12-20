from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

def define_env(env):
    @env.macro
    def get_today(fmt="%Y-%m-%d"):
        return datetime.today().strftime(fmt)

    @env.macro
    def calc_exp(start: str, end: str, fmt: str = "%Y-%m-%d"):
        start_date = datetime.strptime(start, fmt)
        end_date = datetime.strptime(end, fmt)

        diff = relativedelta(end_date, start_date)

        start_formatted = start_date.strftime("%b %Y")
        end_formatted = end_date.strftime("%b %Y")
        
        years_exp = f"{diff.years if diff.years >= 1 else ''} {'yr(s)' if diff.years >= 1 else ''}"
        months_exp = f"{diff.months if diff.months >= 1 else ''} {'mo(s)' if diff.months >= 1 else ''}"

        return f"{start_formatted} - {end_formatted} · {years_exp} {months_exp}"