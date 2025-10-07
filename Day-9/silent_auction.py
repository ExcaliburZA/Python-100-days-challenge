print("\033[H\033[J", end="")
name = input("What is your name? ")
bid = input("What is your bid? $")

bids = {
  name: bid
}

maxBidder = name
maxBid = bids[name]

while True:
  otherBiddersResponse = input("Are there others who need to bid? ")
  if otherBiddersResponse.lower() == "no":
    break
  elif otherBiddersResponse.lower() == "yes":
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bids[name] = bid
    print(f"Bid of ${bid} received for {name}")

    if int(bids[name]) > int(maxBid):
      print(
        f"{maxBidder}'s bid of ${maxBid} was overtaken by {name} with a bid of ${bid}!")
      maxBidder = name
      maxBid = bids[name]
    else:
      print(f"{maxBidder} is still winning with their bid of ${maxBid}!")
  else:
    print("Please enter either 'yes' or 'no' to continue")

print(f"Winner is {maxBidder} with a bid of ${maxBid}!")