# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import GLM


def test_GLM_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    contrasts=dict(argstr='-c %s',
    ),
    dat_norm=dict(argstr='--dat_norm',
    ),
    demean=dict(argstr='--demean',
    ),
    des_norm=dict(argstr='--des_norm',
    ),
    design=dict(argstr='-d %s',
    mandatory=True,
    position=2,
    ),
    dof=dict(argstr='--dof=%d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-i %s',
    mandatory=True,
    position=1,
    ),
    mask=dict(argstr='-m %s',
    ),
    out_cope=dict(argstr='--out_cope=%s',
    ),
    out_data_name=dict(argstr='--out_data=%s',
    ),
    out_f_name=dict(argstr='--out_f=%s',
    ),
    out_file=dict(argstr='-o %s',
    keep_extension=True,
    name_source='in_file',
    name_template='%s_glm',
    position=3,
    ),
    out_p_name=dict(argstr='--out_p=%s',
    ),
    out_pf_name=dict(argstr='--out_pf=%s',
    ),
    out_res_name=dict(argstr='--out_res=%s',
    ),
    out_sigsq_name=dict(argstr='--out_sigsq=%s',
    ),
    out_t_name=dict(argstr='--out_t=%s',
    ),
    out_varcb_name=dict(argstr='--out_varcb=%s',
    ),
    out_vnscales_name=dict(argstr='--out_vnscales=%s',
    ),
    out_z_name=dict(argstr='--out_z=%s',
    ),
    output_type=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    var_norm=dict(argstr='--vn',
    ),
    )
    inputs = GLM.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_GLM_outputs():
    output_map = dict(out_cope=dict(),
    out_data=dict(),
    out_f=dict(),
    out_file=dict(),
    out_p=dict(),
    out_pf=dict(),
    out_res=dict(),
    out_sigsq=dict(),
    out_t=dict(),
    out_varcb=dict(),
    out_vnscales=dict(),
    out_z=dict(),
    )
    outputs = GLM.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
