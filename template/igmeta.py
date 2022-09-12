from igm.conf import igm_project, cpy

igm_project(
    name={{ (user.name | str + '-simple-demo') | potc }},
    version='0.3.2',
    template_name={{ template.name | potc }},
    template_version={{ template.version | potc }},
    created_at={{ py.time.time() | int | potc }},
    scripts={
        None: cpy('main.py')
    }
)
