
class Plane:
    model:str
    zone :list
    
    def __init__(self, model, creg, calc_base, desired_mac_percent, desired_index, 
             index_reference_datum_plane, ird_mac_percent, irdp_index, 
             denominator, zero_percent_mac_h,meanchord, bem, bei, trimfuncgrad, trimfuncdist, 
             flightcrew_h, flightcrew_w, cabincrew_w, fso_w, pax_a_w, 
             pax_c_w, pax_i_w, mzfm, mlm, mtom, mtm, mfw, version, 
             obs, obs_1_h, obs_2_h, attendantseat, 
             ccs_1_h, ccs_2_h, ccs_3_h, ccs_4_h, ccs_5_h, ccs_6_h, 
             cabinzone, cabin_a_h, cabin_a_max, cabin_b_h, cabin_b_max, 
             cabin_c_h, cabin_c_max, cabin_d_h, cabin_d_max, econ_max,   
             row, zone, cargo, cargo_1_h, cargo_1_max, cargo_2_h, cargo_2_max, 
             cargo_3_h, cargo_3_max, cargo_4_h, cargo_4_max, cargo_5_h, cargo_5_max, 
             cargo_6_h, cargo_6_max, pantry, pantry_1_h, pantry_1_max, pantry_e_z, 
             pantry_d, pantry_a, pantry_2_h, pantry_2_max, pantry_2_e_z, 
             pantry_2_d, pantry_2_a, fueltank, innertank_h, innertank_max, outertank_h,
             outertank_max, centertank_h, centertank_max, portwater1_h, portwater1_w,
             wardrobe_h,wardrobe_max, wardrobe_w):
        self.model = model  
        self.creg = creg
        self.calc_base = calc_base
        self.desired_mac_percent = desired_mac_percent
        self.desired_index = desired_index
        self.index_reference_datum_plane = index_reference_datum_plane
        self.ird_mac_percent = ird_mac_percent
        self.irdp_index = irdp_index
        self.denominator = denominator
        self.zero_percent_mac_h = zero_percent_mac_h 
        self.meanchord = meanchord
        self.bem = bem
        self.bei = bei
        self.trimfuncgrad = trimfuncgrad
        self.trimfuncdist = trimfuncdist
        self.flightcrew_h = flightcrew_h
        self.flightcrew_w = flightcrew_w
        self.cabincrew_w = cabincrew_w
        self.fso_w = fso_w
        self.pax_a_w = pax_a_w
        self.pax_c_w = pax_c_w
        self.pax_i_w = pax_i_w
        self.mzfm = mzfm
        self.mlm = mlm
        self.mtom = mtom
        self.mtm = mtm
        self.mfw = mfw
        self.version = version
        self.obs = obs
        self.obs_1_h = obs_1_h
        self.obs_2_h = obs_2_h
        self.attendantseat = attendantseat
        self.ccs_1_h = ccs_1_h
        self.ccs_2_h = ccs_2_h
        self.ccs_3_h = ccs_3_h
        self.ccs_4_h = ccs_4_h
        self.ccs_5_h = ccs_5_h
        self.ccs_6_h = ccs_6_h
        self.cabinzone = cabinzone
        self.cabin_a_h = cabin_a_h
        self.cabin_a_max = cabin_a_max
        self.cabin_b_h = cabin_b_h
        self.cabin_b_max = cabin_b_max
        self.cabin_c_h = cabin_c_h
        self.cabin_c_max = cabin_c_max
        self.cabin_d_h = cabin_d_h
        self.cabin_d_max = cabin_d_max
        self.econ_max = econ_max
        self.row = row
        self.zone = zone 
        self.cargo = cargo
        self.cargo_1_h = cargo_1_h
        self.cargo_1_max = cargo_1_max
        self.cargo_2_h = cargo_2_h
        self.cargo_2_max = cargo_2_max
        self.cargo_3_h = cargo_3_h
        self.cargo_3_max = cargo_3_max
        self.cargo_4_h = cargo_4_h
        self.cargo_4_max = cargo_4_max
        self.cargo_5_h = cargo_5_h
        self.cargo_5_max = cargo_5_max
        self.cargo_6_h = cargo_6_h
        self.cargo_6_max = cargo_6_max
        self.pantry = pantry
        self.pantry_1_h = pantry_1_h
        self.pantry_1_max = pantry_1_max
        self.pantry_e_z = pantry_e_z
        self.pantry_d = pantry_d
        self.pantry_a = pantry_a
        self.pantry_2_h = pantry_2_h
        self.pantry_2_max = pantry_2_max
        self.pantry_2_e_z = pantry_2_e_z
        self.pantry_2_d = pantry_2_d
        self.pantry_2_a = pantry_2_a
        self.fueltank = fueltank
        self.innertank_h = innertank_h
        self.innertank_max = innertank_max
        self.outertank_h = outertank_h
        self.outertank_max = outertank_max
        self.centertank_h = centertank_h
        self.centertank_max = centertank_max
        self.portwater1_h = portwater1_h
        self.portwater1_w = portwater1_w
        self.wardrobe_h = wardrobe_h
        self.wardrobe_max = wardrobe_max
        self.wardrobe_w = wardrobe_w