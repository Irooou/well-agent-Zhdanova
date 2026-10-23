import math


def ipr_vogel(p_res: float, p_test: float, q_test: float, p_wf: float) -> float:
    """Дебит по Вогелю, м3/сут. Давления абсолютные, атм."""
    # TODO B: перенесите сюда рабочий код занятия 3 вместе с проверкой диапазонов
    if not (p_res > 0 and 0 <= p_test < p_res and 0 <= p_wf <= p_res and q_test >= 0):
      raise ValueError("Проверьте диапазон параметров")
    # TODO A: найдите qmax по p_test и q_test
    x = p_test / p_res
    qmax = q_test / (1 - 0.2*x - 0.8*x**2)
    # TODO A: рассчитайте дебит при p_wf и верните его
    x = p_wf / p_res
    q = qmax * (1-0.2*x-0.8*x**2)
    return q


def arps_decline(q0: float, annual_decline: float, years: float) -> float:
    """Экспоненциальный спад дебита, м3/сут."""
    # TODO B: перенесите сюда рабочий код занятия 3
    if not (q0 > 0 and annual_decline >= 0 and years >= 0):
        raise ValueError("Проверьте диапазон параметров. Ожидается q0 > 0, annual_decline >= 0, years >= 0")
    return q0 * math.exp(-annual_decline * years)
