from pypeyuml.depth_first_search import depth_first_search
from pypeyuml.execute_pipelines import execute_pipelines
from pypeyuml.parse_yuml import parse_yuml
from pypeyuml.topological_sort import topological_sort

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 3:
    print("Usage: python main.py <pipelines.yuml> <pipelines_dir>")
    sys.exit(1)

  yuml_path = sys.argv[1]
  pipelines_dir = sys.argv[2]
  
  nodes, edges = parse_yuml(yuml_path)
  
  print("\n➡️  Pipelines:\n")
  print(", ".join(list(nodes.keys())))

  print("\n🔀 Paths:\n")
  paths = depth_first_search(edges)
  for path in paths:
    print(path)
  
  pipeline_order, graph = topological_sort(nodes, edges)
  
  print("\n🔢 Order:\n")
  for i, pipeline in enumerate(pipeline_order):
    print(f"{i + 1:02} {pipeline}")
  
  print("\n▶️  Execution:")
  execute_pipelines(pipelines_dir, pipeline_order, graph, nodes)