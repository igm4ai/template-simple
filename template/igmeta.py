from igm.conf import igm_project

igm_project(
    name={{ (user.name | str + '-simple-demo') | potc }},
    version='0.3.2',
    template_name='igm-simple',
    template_version='0.0.1',
    created_at={{ py.time.time() | potc }},
)
