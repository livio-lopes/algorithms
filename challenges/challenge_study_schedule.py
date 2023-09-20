from collections import Counter


def study_schedule(permanence_period, target_time):
    interval_study = []
    if target_time == 0:
        for start, end in permanence_period:
            if isinstance(start, int) and isinstance(end, int):
                interval_study.extend(list(range(start, end + 1)))
            else:
                return None
            return dict(Counter(interval_study))[target_time]
        return
    elif not target_time or not permanence_period:
        return None
    else:
        for start, end in permanence_period:
            if isinstance(start, int) and isinstance(end, int):
                interval_study.extend(list(range(start, end + 1)))
            else:
                return None
        return dict(Counter(interval_study))[target_time]
    """Faça o código aqui."""
    # raise NotImplementedError


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)]
# print(study_schedule(permanence_period, 5))