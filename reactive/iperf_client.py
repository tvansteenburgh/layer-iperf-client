from charms.reactive import when
from charmhelpers.core.unitdata import kv

kvdb = kv()


@when('iperf.available')
def configure_iperf_server(iperf):
    kvdb.set('server-port', iperf.get_remote('port'))
    kvdb.set('server-host', iperf.get_remote('hostname'))
