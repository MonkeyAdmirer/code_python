def twenty(start=1, end=100, q_count=0:):
    if start > end:
        return "I admit defeat."
    elif q_count == 20:
        return "I admit defeat."
    else:
        mid = (start + end) // 2
        q_count += 1
        user_input = input(f"Is {mid} your value? (Yes/No)")
        if user_input.lower() == 'yes':
            return f"I win with {q_count} questions asked."
        else: 
            q_count += 1
            user_input = input(f"Is your number lower than {mid}? (Yes/No)")
            if user_input.lower() == 'yes':
                return twenty(start, mid-1, q_count)
            else:
                return twenty(mid+1, end, q_count)
