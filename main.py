from collections import defaultdict


class PathFinder:
    def __init__(self, dict_relations):
        self.relations = dict_relations

    def get_vertices(self):
        return list(self.relations.keys())

    def print_all_paths(self, origin, destination):
        visited = dict.fromkeys(set(relations.keys()), False)
        path = list()
        self.__print_all_paths_util(origin, destination, visited, path)

    def __print_all_paths_util(self, origin, destination, visited, path):
        visited[origin] = True
        path.append(origin)

        if origin == destination:
            print(path)
        else:
            for i in self.relations[origin]:
                if not visited[i]:
                    self.__print_all_paths_util(i, destination, visited, path)
        path.pop()
        visited[origin] = False
