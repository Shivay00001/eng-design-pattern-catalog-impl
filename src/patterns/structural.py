# --- Adapter ---
class LegacyPaymentSystem:
    def distinct_pay(self, amount_cents):
        return f"Paid {amount_cents} cents via Legacy"

class NewPaymentInterface:
    def pay(self, dollars):
        pass

class PaymentAdapter(NewPaymentInterface):
    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy = legacy_system

    def pay(self, dollars):
        cents = int(dollars * 100)
        return self.legacy.distinct_pay(cents)

# --- Decorator ---
class Notifier:
    def send(self, msg):
        return f"Email: {msg}"

class SMSDecorator:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, msg):
        base = self.notifier.send(msg)
        return f"{base} + SMS: {msg}"

class SlackDecorator:
    def __init__(self, notifier):
        self.notifier = notifier # Can chain decorators

    def send(self, msg):
        base = self.notifier.send(msg)
        return f"{base} + Slack: {msg}"
