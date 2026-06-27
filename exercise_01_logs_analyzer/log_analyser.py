from functools import reduce
from collections import Counter, defaultdict

logs = [
    "2025-01-01 INFO user_login alice",
    "2025-01-01 ERROR database_failed",
    "2025-01-01 INFO user_login bob",
    "2025-01-02 WARNING disk_space_low",
    "2025-01-02 ERROR database_failed",
    "2025-01-02 INFO user_login alice",
]

def quick_report (*args):
    """Nombre de logs par niveau

    Args:
        args: liste(s) contenant n items suivant l'ordre : date, type et log
        
    Returns:
        count_types (Counter): counter de type de log
    """
    
    args = reduce(lambda x, y: x+y, args)
    count_types = Counter([log.split()[1] for log in args])
    return count_types


def activities_per_user(*args):
    """Nombre de activities par user

    Args:
        args: liste(s) contenant n items suivant l'ordre : date, type, log et user (facultatif)
        
    Returns:
        activities (Counter): counter d'activities par user
    """
    
    args = reduce(lambda x, y: x+y, args)
    
    activities = defaultdict(int)
    users = [log.split()[-1] for log in args if len(log.split()) == 4]
    
    for user in users:
        activities[user] += 1
    
    return activities


def most_common_logs_by_type(*args, type="error", limit=1):
    """Logs les plus courantes pour le type donné

    Args:
        args: liste(s) contenant n items suivant l'ordre : date, type, log et user (facultatif)
        type (str): type de log à renvoyer
        limit (int): le nombre de logs maximal à renvoyer
        
    Returns:
        logs (list): list contenant les logs
    """
    args = reduce(lambda x, y: x+y, args)
    
    logs = [log for log in args if log.split()[1].lower() == type.lower()]
    count_logs = Counter([log.split()[2] for log in logs])
    
    return count_logs.most_common(limit)
    

print(dict(quick_report(logs)))
print(dict(activities_per_user(logs)))
print(most_common_logs_by_type(logs, logs[-2:], type='error', limit=3))