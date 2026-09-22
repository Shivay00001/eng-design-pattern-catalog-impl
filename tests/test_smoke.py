"""Smoke test for eng-design-pattern-catalog-impl: pattern behaviors."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.patterns.creational import DatabaseConnection, SerializerFactory
from src.patterns.structural import LegacyPaymentSystem, PaymentAdapter, Notifier, SMSDecorator
from src.patterns.behavioral import NewsPublisher, NewsChannel, Navigator, RoadStrategy, WalkingStrategy


def main():
    # Singleton
    assert DatabaseConnection() is DatabaseConnection()
    assert DatabaseConnection().query("SELECT 1") == "Executing SELECT 1"

    # Factory
    assert "data" in SerializerFactory.get_serializer("json").serialize("x")
    assert "<data>x</data>" == SerializerFactory.get_serializer("xml").serialize("x")

    # Adapter
    adapter = PaymentAdapter(LegacyPaymentSystem())
    assert adapter.pay(10) == "Paid 1000 cents via Legacy"

    # Decorator
    assert SMSDecorator(Notifier()).send("hi") == "Email: hi + SMS: hi"

    # Observer
    seen = []

    class Rec(NewsChannel):
        def update(self, news):
            seen.append(news)

    pub = NewsPublisher()
    pub.attach(Rec("r1"))
    pub.notify("test-news")
    assert seen == ["test-news"]

    # Strategy
    nav = Navigator(RoadStrategy())
    assert nav.navigate("A", "B") == "Road from A to B"
    nav.set_strategy(WalkingStrategy())
    assert nav.navigate("A", "B") == "Walkpath from A to B"

    print("smoke OK: singleton, factory, adapter, decorator, observer, strategy")


if __name__ == "__main__":
    main()
