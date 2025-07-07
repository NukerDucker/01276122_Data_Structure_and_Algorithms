def vickrey_auction(bids):
    if len(bids) < 2:
        return "not enough bidder"
    
    sorted_bids = sorted(bids, reverse=True)
    winner_bid = sorted_bids[0]
    if winner_bid == sorted_bids[1]:
        return "error : have more than one highest bid"
    return f"winner bid is {winner_bid} need to pay {sorted_bids[1]}"

def main():
    bids = [int(e) for e in input("Enter All Bid : ").split()]
    result = vickrey_auction(bids)
    print(result)
    
if __name__ == "__main__":
    main()