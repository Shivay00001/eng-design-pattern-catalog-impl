from src.patterns.creational import DatabaseConnection, SerializerFactory
from src.patterns.structural import LegacyPaymentSystem, PaymentAdapter, Notifier, SMSDecorator, SlackDecorator
from src.patterns.behavioral import NewsPublisher, NewsChannel, Navigator, RoadStrategy, WalkingStrategy

def main():
    print("--- Design Patterns Implementation Demo ---\n")

    # 1. Singleton
    print("[Singleton]")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Same Instance? {db1 is db2}")
    print(db1.query("SELECT * FROM users"))
    print()

    # 2. Factory
    print("[Factory Method]")
    json_s = SerializerFactory.get_serializer("json")
    print(json_s.serialize("hello"))
    print()

    # 3. Adapter
    print("[Adapter]")
    legacy = LegacyPaymentSystem()
    adapter = PaymentAdapter(legacy)
    print(adapter.pay(50)) # Converts $50 to 5000 cents
    print()

    # 4. Decorator
    print("[Decorator]")
    notifier = Notifier()
    notifier = SMSDecorator(notifier)
    notifier = SlackDecorator(notifier)
    print(notifier.send("Server Down!"))
    print()

    # 5. Observer
    print("[Observer]")
    pub = NewsPublisher()
    pub.attach(NewsChannel("CNN"))
    pub.attach(NewsChannel("BBC"))
    pub.notify("Python 4.0 Released!")
    print()

    # 6. Strategy
    print("[Strategy]")
    nav = Navigator(RoadStrategy())
    print(nav.navigate("Home", "Work"))
    nav.set_strategy(WalkingStrategy())
    print(nav.navigate("Home", "Park"))

if __name__ == "__main__":
    main()
