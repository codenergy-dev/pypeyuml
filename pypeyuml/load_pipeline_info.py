import importlib.util
import os

def load_pipeline_info(pipelines_dir, pipeline_name, venv_aware=False):
  filename = os.path.join(pipelines_dir, f"{pipeline_name}.py")
  if not os.path.exists(filename):
    raise FileNotFoundError(f"File {filename} not found.")

  if venv_aware:
    return None, filename  # Don't load the function if it will run in another venv

  spec = importlib.util.spec_from_file_location(pipeline_name, filename)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  func = getattr(module, pipeline_name)
  return func, filename