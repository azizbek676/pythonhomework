def calculate_investment(principal: float, annual_rate: float, years: int) -> float:
    """Calculates the total investment value after a number of years with a fixed annual rate of return."""
    return principal * (1 + annual_rate / 100) ** years

principal = float(input("Enter the initial deposit (principal amount): "))

annual_rate = float(input("Enter the annual rate of return (as a percentage): "))

years = int(input("Enter the number of years the investment will grow: "))

final_value = calculate_investment(principal, annual_rate, years)
print(f"After {years} years, your investment will be worth: ${final_value:.2f}")