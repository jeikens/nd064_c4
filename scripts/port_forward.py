import subprocess

forwards = [
    {'namespace': 'monitoring', 'service': 'service/prometheus-grafana', 'host_port': '3000', 'svc_port': '80'},
    {'namespace': 'observability', 'service': 'service/proj-tracer-query', 'host_port': '16686', 'svc_port': '16686'},
    {'namespace': 'default', 'service': 'service/frontend-service', 'host_port': '8080', 'svc_port': '8080'},
    {'namespace': 'default', 'service': 'service/backend', 'host_port': '8081', 'svc_port': '8081'},
    {'namespace': 'default', 'service': 'service/trial-service', 'host_port': '8082', 'svc_port': '8082'},
    {'namespace': 'monitoring', 'service': 'service/prometheus-kube-prometheus-prometheus', 'host_port': '8888', 'svc_port': '9090'},

]

proc = []

for frwds in forwards:
    proc.append(subprocess.Popen([
        'kubectl',
        'port-forward',
        '-n',
        frwds['namespace'],
        frwds['service'],
        '--address',
        '0.0.0.0',
        frwds['host_port']+':'+frwds['svc_port']
    ]))

input()
for p in proc:
    p.terminate()
