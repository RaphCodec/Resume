from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def define_env(env):

    @env.macro
    def get_today(fmt="%Y-%m-%d"):
        return date.today().strftime(fmt)

    @env.macro
    def calc_exp(start: str, end: str=None, fmt: str="%Y-%m-%d", time_only: bool=False):
        start_date = datetime.strptime(start, fmt)

        if end:
            end_date = datetime.strptime(end, fmt)
        else:
            # default end is today
            end_date = datetime.combine(date.today(), datetime.min.time())

        diff = relativedelta(end_date, start_date)

        start_formatted = start_date.strftime("%b %Y")

        # check for end == today
        if end and end_date.date() == date.today():
            end_formatted = "Present"
        elif not end:
            end_formatted = "Present"
        else:
            end_formatted = end_date.strftime("%b %Y")

        parts = []
        if diff.years and diff.years > 1:
            parts.append(f"{diff.years} yrs")
        elif diff.years:
            parts.append(f"{diff.years} yr")
        if diff.months and diff.months > 1:
            parts.append(f"{diff.months} mos")
        elif diff.months:
            parts.append(f"{diff.months} mo")

        exp = " ".join(parts) if parts else "0 mos"

        if time_only:
            return exp
        
        return f"{start_formatted} - {end_formatted} · {exp}"
