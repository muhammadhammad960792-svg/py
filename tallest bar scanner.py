
# ==========================================
# PROJECT: TALLEST BAR SCANNER
# Language: Python
# ==========================================

print("====================================")
print("         TALLEST BAR SCANNER")
print("====================================")


# STEP 1: Create the stock price list

prices = [7, 1, 5, 3, 6, 4]

print("\nStep 1: Stock Price List")
print("Prices:", prices)


# STEP 2: Calculate stock buy-sell profit

profit = 0

for i in range(1, len(prices)):

    if prices[i] > prices[i - 1]:

        gain = prices[i] - prices[i - 1]
        profit += gain

print("\nStep 2: Stock Buy-Sell Profit")
print("Profit:", profit)


# STEP 3: Accumulate every positive difference

total_profit = 0

for i in range(1, len(prices)):

    difference = prices[i] - prices[i - 1]

    if difference > 0:
        total_profit += difference

print("\nStep 3: Total Accumulated Profit")
print("Total Profit:", total_profit)


# STEP 4: Build the left tallest bars list

heights = [4, 2, 0, 3, 2, 5]

left_tallest = []

left_max = heights[0]

for height in heights:

    left_max = max(left_max, height)
    left_tallest.append(left_max)

print("\nStep 4: Left Tallest Bars")
print("Heights:", heights)
print("Left Tallest:", left_tallest)


# STEP 5: Build the right tallest bars list

right_tallest = [0] * len(heights)

right_max = heights[-1]

for i in range(len(heights) - 1, -1, -1):

    right_max = max(right_max, heights[i])
    right_tallest[i] = right_max

print("\nStep 5: Right Tallest Bars")
print("Right Tallest:", right_tallest)


# STEP 6: Calculate trapped rainwater

total_water = 0

for i in range(len(heights)):

    water_level = min(left_tallest[i], right_tallest[i])

    water = water_level - heights[i]

    total_water += water

print("\nStep 6: Trapped Rainwater")
print("Total Trapped Water:", total_water)


# FINAL RESULT

print("\n====================================")
print("          SCAN COMPLETED")
print("====================================")

print("Stock Profit:", profit)
print("Accumulated Profit:", total_profit)
print("Trapped Rainwater:", total_water)

print("====================================")
print("       THANK YOU FOR USING")
print("       TALLEST BAR SCANNER")
print("====================================")
