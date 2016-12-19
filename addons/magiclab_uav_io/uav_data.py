from mathutils import Vector
"""
Snapshoted Blender data for creating meshes and materials
Includes some console funcs to import the data into the file,
usage:
load uav_data.py (this file) into a blender text editor
in the console :
import uav_data
in the text editor:
delete the data and leave the cursor where it started.
in the console:
uav_data.get_console(D.materials["source_material"], D.text['uav_data'])
check the materials resulting and hand add any missing properties.
"""
sphere_verts = [(-0.057569846510887146, -0.05756986141204834, -0.057569846510887146), (-0.057569846510887146, -0.057569846510887146, 0.057569846510887146), (-0.057569846510887146, 0.05756983906030655, -0.057569846510887146), (-0.057569846510887146, 0.05756986141204834, 0.05756986141204834), (0.057569846510887146, -0.057569846510887146, -0.057569846510887146), (0.057569846510887146, -0.05756983906030655, 0.05756983906030655), (0.05756986141204834, 0.05756986141204834, -0.057569846510887146), (0.057569846510887146, 0.05756983906030655, 0.057569846510887146), (-0.07050837576389313, 3.8081367920161924e-11, -0.07050837576389313), (-0.07050837576389313, -0.07050836831331253, 1.0825736140862574e-10), (-0.07050837576389313, 3.8083057540827525e-11, 0.07050837576389313), (-0.07050838321447372, 0.07050837576389313, 1.0825900592648097e-10), (7.788127781571674e-12, 0.07050837576389313, -0.07050837576389313), (7.7883498261766e-12, 0.07050837576389313, 0.07050837576389313), (0.07050837576389313, 0.07050838321447372, 1.0825809693137955e-10), (0.07050837576389313, 3.8082967335206774e-11, -0.07050837576389313), (0.07050837576389313, 3.8083057540827525e-11, 0.07050837576389313), (0.07050838321447372, -0.07050837576389313, 1.0825900592648097e-10), (7.788127781571674e-12, -0.07050838321447372, -0.07050837576389313), (7.788172017020312e-12, -0.07050837576389313, 0.07050838321447372), (7.788127781571674e-12, 3.8082967335206774e-11, 0.09971390664577484), (7.788571870781524e-12, 3.8083057540827525e-11, -0.09971389919519424), (7.786529233888562e-12, -0.09971389919519424, 1.0825736140862574e-10), (0.09971389919519424, 3.8083057540827525e-11, 1.0825736140862574e-10), (7.788260487917587e-12, 0.09971389919519424, 1.0825900592648097e-10), (-0.09971389919519424, 3.8083057540827525e-11, 1.0825736140862574e-10), (-0.06719592958688736, -0.030203886330127716, -0.06719593703746796), (-0.06719593703746796, -0.06719592958688736, 0.030203886330127716), (-0.06719593703746796, 0.030203886330127716, 0.06719593703746796), (-0.06719595193862915, 0.06719593703746796, -0.030203888192772865), (-0.030203886330127716, 0.06719593703746796, -0.06719592958688736), (0.030203882604837418, 0.06719593703746796, 0.06719592958688736), (0.06719592958688736, 0.06719593703746796, -0.030203886330127716), (0.06719592958688736, 0.030203886330127716, -0.06719593703746796), (0.06719593703746796, -0.030203886330127716, 0.06719593703746796), (0.06719593703746796, -0.06719593703746796, -0.030203886330127716), (0.030203886330127716, -0.06719593703746796, -0.06719595193862915), (-0.030203886330127716, -0.06719593703746796, 0.06719592958688736), (-0.06719592958688736, 0.030203886330127716, -0.06719593703746796), (-0.06719593703746796, -0.06719593703746796, -0.030203888192772865), (-0.06719593703746796, -0.030203886330127716, 0.06719593703746796), (-0.06719593703746796, 0.06719593703746796, 0.030203886330127716), (0.030203886330127716, 0.06719593703746796, -0.06719592958688736), (-0.030203886330127716, 0.06719593703746796, 0.06719592958688736), (0.06719593703746796, 0.06719593703746796, 0.030203886330127716), (0.06719593703746796, -0.030203886330127716, -0.06719593703746796), (0.06719592958688736, 0.030203886330127716, 0.06719593703746796), (0.06719593703746796, -0.06719593703746796, 0.030203886330127716), (-0.030203886330127716, -0.06719593703746796, -0.06719593703746796), (0.030203888192772865, -0.06719592958688736, 0.06719595193862915), (7.786529233888562e-12, -0.03815886005759239, 0.09212364256381989), (7.788172017020312e-12, 0.03815886750817299, 0.09212364256381989), (0.03815886378288269, 3.8082967335206774e-11, 0.09212364256381989), (-0.03815886378288269, 3.8082967335206774e-11, 0.09212364256381989), (7.788127781571674e-12, -0.03815886750817299, -0.09212364256381989), (7.787772163259099e-12, 0.03815886378288269, -0.09212363511323929), (-0.03815886750817299, 3.8082967335206774e-11, -0.09212364256381989), (0.03815886750817299, 3.8081458125782675e-11, -0.09212363511323929), (-0.03815886378288269, -0.09212364256381989, 1.0825736140862574e-10), (0.03815886378288269, -0.09212363511323929, 1.0825736140862574e-10), (7.788971724542737e-12, -0.09212364256381989, -0.03815886750817299), (7.788127781571674e-12, -0.09212364256381989, 0.03815886378288269), (0.09212364256381989, -0.038158852607011795, 1.0825727120300499e-10), (0.09212363511323929, 0.038158856332302094, 1.0825736140862574e-10), (0.09212364256381989, 3.8083411424416624e-11, -0.03815886378288269), (0.09212363511323929, 3.8083057540827525e-11, 0.03815886378288269), (0.03815886005759239, 0.09212364256381989, 1.0825736140862574e-10), (-0.03815886378288269, 0.09212363511323929, 1.0825736140862574e-10), (7.788172017020312e-12, 0.09212363511323929, -0.03815886378288269), (7.788127781571674e-12, 0.09212364256381989, 0.03815886378288269), (-0.09212363511323929, 0.038158856332302094, 1.0825736140862574e-10), (-0.09212364256381989, -0.03815886750817299, 1.0825748630871601e-10), (-0.09212364256381989, 3.8082967335206774e-11, -0.03815886750817299), (-0.09212364256381989, 3.8082967335206774e-11, 0.03815886378288269), (-0.08544090390205383, -0.03603626787662506, 0.03666200861334801), (-0.08544090390205383, -0.036036256700754166, -0.03666200488805771), (-0.08544090390205383, 0.03603626787662506, -0.03666200488805771), (-0.03603627160191536, 0.08544090390205383, 0.03666200488805771), (-0.03603626787662506, 0.08544090390205383, -0.03666200861334801), (0.03603627532720566, 0.08544091135263443, -0.036662012338638306), (0.08544090390205383, 0.03603626787662506, 0.03666200116276741), (0.08544091135263443, 0.03603627532720566, -0.03666200861334801), (0.08544090390205383, -0.03603626787662506, -0.03666200488805771), (0.03603626787662506, -0.08544090390205383, 0.03666200488805771), (0.03603626787662506, -0.08544090390205383, -0.03666200861334801), (-0.03603626787662506, -0.08544090390205383, -0.03666200861334801), (0.03666200488805771, 0.03603626787662506, -0.08544090390205383), (-0.03666200488805771, 0.03603626787662506, -0.08544090390205383), (-0.03666200861334801, -0.03603627532720566, -0.08544091135263443), (-0.03666200488805771, 0.03603627160191536, 0.08544090390205383), (0.03666200861334801, 0.03603626787662506, 0.08544090390205383), (0.03666200861334801, -0.03603626787662506, 0.08544090390205383), (-0.03666200861334801, -0.03603627532720566, 0.08544091135263443), (0.03666200488805771, -0.03603626787662506, -0.08544090390205383), (-0.03603626787662506, -0.08544090390205383, 0.03666200116276741), (0.08544090390205383, -0.03603626787662506, 0.03666200488805771), (0.03603627160191536, 0.08544090390205383, 0.03666200488805771), (-0.08544090390205383, 0.03603627532720566, 0.03666200861334801)]
sphere_faces = [(70, 97, 41, 11), (40, 1, 37, 92), (61, 83, 49, 19), (75, 39, 9, 71), (94, 61, 19, 37), (95, 34, 5, 47), (89, 43, 3, 28), (97, 73, 10, 28), (40, 10, 73, 74), (37, 1, 27, 94), (92, 53, 10, 40), (95, 65, 16, 34), (91, 34, 16, 52), (92, 50, 20, 53), (88, 26, 8, 56), (54, 21, 57, 93), (85, 48, 18, 60), (62, 95, 47, 17), (58, 22, 61, 94), (83, 59, 17, 47), (93, 57, 15, 45), (36, 4, 35, 84), (86, 42, 6, 33), (66, 96, 44, 14), (62, 23, 65, 95), (14, 44, 80, 63), (86, 55, 12, 42), (33, 6, 32, 81), (87, 38, 2, 30), (79, 68, 24, 66), (66, 24, 69, 96), (67, 11, 41, 77), (56, 8, 38, 87), (30, 2, 29, 78), (48, 85, 39, 0), (88, 48, 0, 26), (25, 71, 74, 73), (51, 13, 43, 89), (24, 67, 77, 69), (30, 78, 68, 12), (16, 46, 90, 52), (23, 63, 80, 65), (22, 59, 83, 61), (36, 84, 60, 18), (21, 55, 86, 57), (20, 51, 89, 53), (19, 50, 92, 37), (49, 83, 47, 5), (5, 34, 91, 49), (80, 44, 7, 46), (46, 7, 31, 90), (43, 77, 41, 3), (85, 60, 22, 58), (81, 63, 23, 64), (82, 45, 15, 64), (40, 74, 27, 1), (88, 54, 18, 48), (87, 55, 21, 56), (75, 71, 25, 72), (84, 59, 22, 60), (86, 33, 15, 57), (79, 42, 12, 68), (76, 38, 8, 72), (97, 70, 25, 73), (29, 76, 70, 11), (77, 43, 13, 69), (58, 9, 39, 85), (91, 52, 20, 50), (38, 76, 29, 2), (96, 31, 7, 44), (90, 51, 20, 52), (26, 75, 72, 8), (42, 79, 32, 6), (82, 64, 23, 62), (45, 82, 35, 4), (84, 35, 17, 59), (9, 27, 74, 71), (33, 81, 64, 15), (75, 26, 0, 39), (97, 28, 3, 41), (65, 80, 46, 16), (96, 69, 13, 31), (28, 10, 53, 89), (76, 72, 25, 70), (93, 45, 4, 36), (88, 56, 21, 54), (19, 49, 91, 50), (35, 82, 62, 17), (78, 67, 24, 68), (32, 79, 66, 14), (9, 58, 94, 27), (90, 31, 13, 51), (78, 29, 11, 67), (81, 32, 14, 63), (18, 54, 93, 36), (87, 30, 12, 55)]
mat_nodes = {'Output': {'height': 100.0, 'select': False, 'hide': False, 'width': 140.0, 'location': (273.77752685546875, 189.1846466064453), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeOutput', 'mute': False, 'name': 'Output'}, 'BLINK_C': {'height': 100.0, 'select': False, 'hide': False, 'width': 140.0, 'location': (-639.87841796875, 171.13571166992188), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeValue', 'mute': False, 'name': 'BLINK_C'}, 'Material Output': {'height': 100.0, 'select': False, 'hide': False, 'width': 140.0, 'location': (455.21246337890625, 354.8165283203125), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeOutputMaterial', 'mute': False, 'name': 'Material Output'}, 'Math': {'height': 100.0, 'select': False, 'hide': False, 'width': 140.0, 'location': (2.8741836547851562, 163.7876434326172), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeMath', 'mute': False, 'name': 'Math', 'operation': 'MULTIPLY', 'use_clamp': True}, 'Value.001': {'height': 100.0, 'select': True, 'hide': False, 'width': 140.0, 'location': (-631.047607421875, 331.36029052734375), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeValue', 'mute': False, 'name': 'Value.001'}, 'Math.003': {'height': 100.0, 'select': False, 'hide': False, 'width': 140.0, 'location': (-215.04531860351562, 46.417205810546875), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeMath', 'mute': False, 'name': 'Math.003', 'operation': 'ADD', 'use_clamp': True}, 'Emission': {'height': 100.0, 'select': False, 'hide': False, 'width': 140.0, 'location': (284.8377685546875, 354.58447265625), 'width_hidden': 42.0, 'label': '', 'bl_idname': 'ShaderNodeEmission', 'mute': False, 'name': 'Emission'}}
mat_links = [{'from_node': {'name': 'Value.001'}, 'to_node': {'name': 'Math'}, 'to_socket': {'name': 'Value', 'index': 0}, 'from_socket': {'name': 'Value', 'index': 0}}, {'from_node': {'name': 'BLINK_C'}, 'to_node': {'name': 'Math.003'}, 'to_socket': {'name': 'Value', 'index': 0}, 'from_socket': {'name': 'Value', 'index': 0}}, {'from_node': {'name': 'Emission'}, 'to_node': {'name': 'Material Output'}, 'to_socket': {'name': 'Surface', 'index': 0}, 'from_socket': {'name': 'Emission', 'index': 0}}, {'from_node': {'name': 'Math'}, 'to_node': {'name': 'Emission'}, 'to_socket': {'name': 'Color', 'index': 0}, 'from_socket': {'name': 'Value', 'index': 0}}, {'from_node': {'name': 'Math.003'}, 'to_node': {'name': 'Math'}, 'to_socket': {'name': 'Value', 'index': 1}, 'from_socket': {'name': 'Value', 'index': 0}}, {'from_node': {'name': 'Math'}, 'to_node': {'name': 'Output'}, 'to_socket': {'name': 'Color', 'index': 0}, 'from_socket': {'name': 'Value', 'index': 0}}]
mat_drivers = [{'variables': [{'type': 'SINGLE_PROP', 'targets': [{'data_path': 'glow'}]}], 'keyframe_points': [{'handle_left_type': 'AUTO', 'handle_left': (-0.09829871356487274, 0.0), 'handle_right_type': 'AUTO', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (0.09829871356487274, 0.0), 'back': 1.7015800476074219, 'co': (0.0, 0.0), 'amplitude': 0.800000011920929, 'interpolation': 'LINEAR', 'period': 4.099999904632568}, {'handle_left_type': 'AUTO_CLAMPED', 'handle_left': (0.15348361432552338, 0.015061158686876297), 'handle_right_type': 'AUTO_CLAMPED', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (0.34868937730789185, 0.08555835485458374), 'back': 1.7015800476074219, 'co': (0.2517823278903961, 0.05056105554103851), 'amplitude': 0.800000011920929, 'interpolation': 'LINEAR', 'period': 4.099999904632568}, {'handle_left_type': 'AUTO', 'handle_left': (0.40309298038482666, 0.07218515872955322), 'handle_right_type': 'AUTO', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (0.5667622685432434, 0.25427699089050293), 'back': 1.7015800476074219, 'co': (0.5, 0.18000000715255737), 'amplitude': 0.800000011920929, 'interpolation': 'LINEAR', 'period': 4.099999904632568}, {'handle_left_type': 'AUTO_CLAMPED', 'handle_left': (0.6042425632476807, 0.3423672318458557), 'handle_right_type': 'AUTO_CLAMPED', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (0.7372519373893738, 0.5993009805679321), 'back': 1.7015800476074219, 'co': (0.6710048317909241, 0.4713316559791565), 'amplitude': 0.800000011920929, 'interpolation': 'LINEAR', 'period': 4.099999904632568}, {'handle_left_type': 'AUTO_CLAMPED', 'handle_left': (0.7744430303573608, 0.7325481176376343), 'handle_right_type': 'AUTO_CLAMPED', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (0.9028865098953247, 0.9366340637207031), 'back': 1.7015800476074219, 'co': (0.8406901359558105, 0.8378092050552368), 'amplitude': 0.800000011920929, 'interpolation': 'LINEAR', 'period': 4.099999904632568}, {'handle_left_type': 'AUTO', 'handle_left': (0.9378036260604858, 1.0), 'handle_right_type': 'AUTO', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (1.0621963739395142, 1.0), 'back': 1.7015800476074219, 'co': (1.0, 1.0), 'amplitude': 0.800000011920929, 'interpolation': 'LINEAR', 'period': 4.099999904632568}], 'data_path': 'nodes["Value.001"].outputs[0].default_value', 'driver': {'type': 'AVERAGE'}, 'array_index': 0}, {'variables': [{'type': 'SINGLE_PROP', 'targets': [{'data_path': 'glow'}]}], 'keyframe_points': [{'handle_left_type': 'VECTOR', 'handle_left': (-0.6663333177566528, 1.3333333730697632), 'handle_right_type': 'VECTOR', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (0.6663333177566528, 0.6666666269302368), 'back': 1.7015800476074219, 'co': (0.0, 1.0), 'amplitude': 0.800000011920929, 'interpolation': 'CONSTANT', 'period': 4.099999904632568}, {'handle_left_type': 'VECTOR', 'handle_left': (1.3326666355133057, 0.3333333432674408), 'handle_right_type': 'VECTOR', 'easing': 'AUTO', 'type': 'KEYFRAME', 'handle_right': (2.6653332710266113, -0.3333333432674408), 'back': 1.7015800476074219, 'co': (1.9989999532699585, 0.0), 'amplitude': 0.800000011920929, 'interpolation': 'CONSTANT', 'period': 4.099999904632568}], 'data_path': 'nodes["Math.003"].inputs[1].default_value', 'driver': {'type': 'AVERAGE'}, 'array_index': 0}]
mat_fcurves = [{'array_index': 0, 'keyframe_points': [{'handle_left_type': 'AUTO_CLAMPED', 'handle_right_type': 'AUTO_CLAMPED', 'type': 'KEYFRAME', 'easing': 'AUTO', 'handle_right': (121.0, 1.0), 'back': 1.7015800476074219, 'period': 4.099999904632568, 'amplitude': 0.800000011920929, 'co': (120.0, 1.0), 'handle_left': (119.0, 1.0), 'interpolation': 'BEZIER'}], 'data_path': 'nodes["BLINK_C"].outputs[0].default_value', 'modifiers': [{'type': 'FNGENERATOR', 'use_additive': False, 'amplitude': 0.5, 'function_type': 'SIN', 'value_offset': 0.5, 'phase_offset': 0.0, 'phase_multiplier': 0.5}]}]


def get_keyframe_points(curve):
    """ Console func helper, gets kp props """
    kp_props = [
        'amplitude', 'back', 'co', 'easing', 'handle_left',
        'handle_left_type', 'handle_right', 'handle_right_type',
        'interpolation', 'period', 'type']
    kps = []
    for k in curve.keyframe_points:
        kp = {}
        for p in kp_props:
            value = getattr(k, p)
            if type(value) == Vector:
                value = tuple(value)
            kp[p] = value
        kps.append(kp)
    return kps


def get_console(mat, text, which='links'):
    """ Console func that copies data to a text file """
    node_values = [
        'bl_idname', 'height', 'width', 'width_hidden',
        'mute', 'hide', 'label', 'location', 'select']
    if which == 'links':
        things = [{
            'from_socket': {
                'name': link.from_socket.name,
                'index': link.from_socket.getIndex()},
            'from_node': {'name': link.from_node.name},
            'to_socket': {
                'name': link.to_socket.name,
                'index': link.to_socket.getIndex()},
            'to_node':{
                'name': link.to_node.name}} for link in mat.node_tree.links]
    elif which == 'nodes':
        things = {
            node.name: {
                attr: getattr(node, attr)
                for attr in node_values if attr in dir(node)} 
            for node in mat.node_tree.nodes}
    elif which == 'drivers':
        things = [{
            'data_path': driver.data_path, 'array_index': driver.array_index,
            'driver': {'type': driver.driver.type, },
            'variables': [{'type': v.type,'targets': [
                {'data_path': t.data_path} for t in v.targets]}
                for v in driver.driver.variables],
            'keyframe_points': get_keyframe_points(driver)
            } for driver in mat.node_tree.animation_data.drivers]
    elif which == 'fcurves':
        things = [{
            'data_path': fc.data_path, 'array_index': fc.array_index,
            'modifiers': [{
                'type': m.type, 'function_type': m.function_type,
                'use_additive': m.use_additive, 'amplitude': m.amplitude,
                'phase_multiplier': m.phase_multiplier,
                'value_offset': m.value_offset,
                'phase_offset': m.phase_offset}for m in fc.modifiers],
            'keyframe_points': get_keyframe_points(fc)
            } for fc in mat.node_tree.animation_data.action.fcurves]
    elif which == 'object_fcurves':
        ob = mat
        things = [{
            'data_path': fc.data_path, 'array_index': fc.array_index,
            'modifiers': [{
                'type': m.type, 'function_type': m.function_type,
                'use_additive': m.use_additive, 'amplitude': m.amplitude,
                'phase_multiplier': m.phase_multiplier,
                'value_offset': m.value_offset,
                'phase_offset': m.phase_offset}for m in fc.modifiers],
            'keyframe_points': get_keyframe_points(fc)
            } for fc in ob.animation_data.action.fcurves]
    elif which == 'object_drivers':
        ob = mat
        things = [{
            'data_path': driver.data_path, 'array_index': driver.array_index,
            'driver': {'type': driver.driver.type, },
            'variables': [{'type': v.type,'targets': [
                {'data_path': t.data_path} for t in v.targets]}
                for v in driver.driver.variables],
            'keyframe_points': get_keyframe_points(driver)
            } for driver in ob.animation_data.drivers]
    elif which == 'mat_drivers':
        things = [{
            'data_path': driver.data_path, 'array_index': driver.array_index,
            'driver': {'type': driver.driver.type, },
            'variables': [{'type': v.type,'targets': [
                {'data_path': t.data_path} for t in v.targets]}
                for v in driver.driver.variables],
            'keyframe_points': get_keyframe_points(driver)
            } for driver in mat.animation_data.drivers]
    text.write(things.__repr())