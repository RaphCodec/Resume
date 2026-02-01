import { differenceInMonths, differenceInYears, format, parse } from 'date-fns';

export function calcExp(start: string, end?: string, fmt = 'yyyy-MM-dd'): string {
  const startDate = parse(start, fmt, new Date());
  const endDate = end ? parse(end, fmt, new Date()) : new Date();

  const years = differenceInYears(endDate, startDate);
  const months = differenceInMonths(endDate, startDate) % 12;

  const startFormatted = format(startDate, 'MMM yyyy');
  const endFormatted = end ? format(endDate, 'MMM yyyy') : 'Present';

  const parts: string[] = [];
  if (years > 0) {
    parts.push(`${years} yr${years > 1 ? 's' : ''}`);
  }
  if (months > 0) {
    parts.push(`${months} mo${months > 1 ? 's' : ''}`);
  }

  const exp = parts.length > 0 ? parts.join(' ') : '0 mos';
  return `${startFormatted} - ${endFormatted} · ${exp}`;
}
