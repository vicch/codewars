def format_duration(n):
	if n <= 0:
		return "now"

	second, n = n % 60, int(n / 60)
	minute, n = n % 60, int(n / 60)
	hour, n = n % 24, int(n / 24)
	day, n = n % 365, int(n / 365)
	year = n

	parts = [
		time_part(year, "year"),
		time_part(day, "day"),
		time_part(hour, "hour"),
		time_part(minute, "minute"),
		time_part(second, "second"),
	]

	parts = [p for p in parts if p != ""]

	if len(parts) > 1:
		return ", ".join(parts[:-1]) + " and " + parts[-1]
	else:
		return parts[0]

def time_part(n, unit):
	return "%s %s" % (n, unit + "s" if n > 1 else unit) if n > 0 else ""

print(format_duration(0))
print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
print(format_duration(12231234))