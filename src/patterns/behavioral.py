from typing import List

# --- Observer ---
class Subscriber:
    def update(self, news):
        pass

class NewsChannel(Subscriber):
    def __init__(self, name):
        self.name = name
    
    def update(self, news):
        print(f"[{self.name}] Breaking News: {news}")

class NewsPublisher:
    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self, news):
        for sub in self._subscribers:
            sub.update(news)

# --- Strategy ---
class RouteStrategy:
    def build_route(self, a, b):
        pass

class RoadStrategy(RouteStrategy):
    def build_route(self, a, b):
        return f"Road from {a} to {b}"

class WalkingStrategy(RouteStrategy):
    def build_route(self, a, b):
        return f"Walkpath from {a} to {b}"

class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def navigate(self, start, end):
        return self._strategy.build_route(start, end)
