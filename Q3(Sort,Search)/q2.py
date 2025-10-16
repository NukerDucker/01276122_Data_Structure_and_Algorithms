def can_check(c, k, weights):
    boxes_needed, current_box_weight = 1, 0
    for weight in weights:
        if weight > c:
            return False
        current_box_weight, boxes_needed = (current_box_weight + weight, boxes_needed) if current_box_weight + weight <= c else (weight, boxes_needed + 1)
    return boxes_needed <= k

def find_min_capacity(weights, boxes):
    l_bound, u_bound = max(weights), sum(weights)
    while l_bound <= u_bound:
        mid = (l_bound + u_bound) // 2
        u_bound, l_bound = (mid - 1, l_bound) if can_check(mid, boxes, weights) else (u_bound, mid + 1)
    return l_bound

if __name__ == '__main__':
    items_weight, boxes = input("Enter Input : ").split('/')
    weights = list(map(int, items_weight.split()))
    boxes = int(boxes)
    print(f'Minimum weigth for {boxes} box(es) = {find_min_capacity(weights, boxes)}')