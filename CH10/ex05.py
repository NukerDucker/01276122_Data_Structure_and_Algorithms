# ex05.py for Chapter 10
def can_check(c, k, weights):
    boxes_needed = 1
    current_box_weight = 0

    for weight in weights:
        if weight > c:
            return False

        if current_box_weight + weight <= c:
            current_box_weight += weight
        else:
            boxes_needed += 1
            current_box_weight = weight

    return boxes_needed <= k

def main():
    items_weight, boxes = input("Enter Input : ").split('/')
    boxes = int(boxes)
    items_weight = list(map(int, items_weight.split()))

    l_bound = max(items_weight)
    u_bound = sum(items_weight)
    min_capacity = u_bound

    while l_bound <= u_bound:
        mid = l_bound + (u_bound - l_bound) // 2
        if can_check(mid, boxes, items_weight):
            min_capacity = mid
            u_bound = mid - 1
        else:
            l_bound = mid + 1

    print(f'Minimum weigth for {boxes} box(es) = {min_capacity}')

if __name__ == '__main__':
    main()