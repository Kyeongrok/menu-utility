
def map_url(pathname, url):
    # Extract the base pattern from pathname
    # For "/plc/UUID/chart" -> "/plc/chart"
    parts = pathname.split('/')
    if len(parts) >= 4:  # Check if path has enough parts
        # Check if third part is either UUID (36 chars) or numeric
        if len(parts[2]) == 36 or parts[2].isdigit():
            base_pattern = f"/{parts[1]}/{parts[3]}"
        else:
            base_pattern = pathname
    else:
        base_pattern = pathname

    # Compare with target URL
    return base_pattern == url

# True를 반환하는 경우
result1 = map_url("/plc/0004221A-5525-473D-A8B2-7E5CB667BFD3/chart", "/plc/chart")  # True

print(result1)

# False를 반환하는 경우
result3 = map_url("/plc/0004221A-5525-473D-A8B2-7E5CB667BFD3/chart", "/plc/log")  # False
print(result3)