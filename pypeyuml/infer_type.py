def infer_type(value: str):
  value = value.strip()
  if value.lower() in ("true", "false"):
    return value.lower() == "true"
  if value.lower() == "none":
    return None
  try:
    if '.' in value:
      return float(value)
    return int(value)
  except ValueError:
    return value  # fallback to string