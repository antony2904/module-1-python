#Create an abstract class Payment with abstract methods make_payment() and payment_status(). 
#Implement two concrete classes CreditCardPayment and UPIPayment. 
#Write a program where the user chooses the payment method and the respective class handles the process.

from abc import ABC, abstractmethod


class Payment(ABC):

  def __init__(self, amount: float):
    self.amount = amount
    self.is_successful = False

  @abstractmethod
  def make_payment(self):
    """Process the payment transaction."""
    pass

  @abstractmethod
  def payment_status(self):
    """Display the status of the transaction."""
    pass


class CreditCardPayment(Payment):

  def __init__(self, amount: float, card_number: str, cvv: str):
    super().__init__(amount)
    self.card_number = card_number
    self.cvv = cvv

  def make_payment(self):
    masked_card = f"****-****-****-{self.card_number[-4:]}"
    print(f"\nAuthorizing ${self.amount:.2f} via Credit Card ({masked_card})...")
    self.is_successful = True
    print("Bank authorization confirmed.")

  def payment_status(self):
    status = "SUCCESS" if self.is_successful else "FAILED"
    print(f"[Credit Card Gateway] Status: {status} | Charged: ${self.amount:.2f}")


class UPIPayment(Payment):

  def __init__(self, amount: float, upi_id: str):
    super().__init__(amount)
    self.upi_id = upi_id

  def make_payment(self):
    print(
        f"\nSending payment request of ${self.amount:.2f} to UPI ID:"
        f" {self.upi_id}..."
    )
    self.is_successful = True
    print("UPI PIN verified.")

  def payment_status(self):
    status = "SUCCESS" if self.is_successful else "FAILED"
    print(f"[UPI Gateway] Status: {status} | Transferred: ${self.amount:.2f}")


def main():
  print("--Payment_Gateway--")
  try:
    amount = float(input("Enter amount to pay: "))
  except ValueError:
    print("Invalid amount entered.")
    return

  print("\nSelect Payment Method:")
  print("1. Credit Card")
  print("2. UPI")
  choice = input("Enter your choice (1 or 2): ").strip()

  payment_gate: Payment

  if choice == "1":
    card_number = input("Enter 16-digit Card Number: ").strip()
    cvv = input("Enter 3-digit CVV: ").strip()
    payment_gate = CreditCardPayment(amount, card_number, cvv)

  elif choice == "2":
    upi_id = input("Enter UPI ID (e.g., user@bank): ").strip()
    payment_gate = UPIPayment(amount, upi_id)

  else:
    print("Invalid payment option selected.")
    return

  payment_gate.make_payment()
  payment_gate.payment_status()


if __name__ == "__main__":
  main()