class Particle:
    """A representation of an entity that can be detected by the C.M.S.""" 
    def __init__(self, e, px, py, pz): 
        self.energy = e 
        self.x_coord = px 
        self.y_coord = py 
        self.z_coord = pz 
        # self.charge = q

    def __repr__(self): 
        return u'<Particle: Energy = {} GeV, Coordinates (X = {}, Y = {}, Z = {})>'\
        .format(self.energy, self.x_coord, self.y_coord, self.z_coord) 

class Jet(Particle): 
    """This is a spray of many particles pulled from a vacuum inside an accelerator."""
    # b_quark_jet_tag

    def __init__(self, e, px, py, pz, b_quark_jet_tag): 
        # Invoke the Particle super class __init__ method first
        Particle.__init__(self, e, px, py, pz)

        # Then initialize the individual members of the Jet class
        self.bottom_quark_jet_tag = b_quark_jet_tag

    def __repr__(self): 
        return u'<Jet: Energy = {} Gev, Coordinates(X = {}, Y = {}, Z = {}), Bottom quark jet tag = {}>'.\
        format(self.energy, self.x_coord, self.y_coord, self.z_coord, self.bottom_quark_jet_tag)

class Lepton(Particle): 
    """Made up of Muons and Electrons, these are negatively charged particles which have antimatter counterparts."""
    # charge 

    def __init__(self, type, e, px, py, pz, q): 
        # Invoke the Particle super class __init__ method first 
        Particle.__init__(self, e, px, py, pz) 

        # Then initialize the charge info for a lepton 
        self.type = type # Whether it is an Electron or a muon 
        self.charge = q

    def __repr__(self): 
        return u'<{}: Energy = {} Gev, Coordinates (X = {}, Y = {}, Z = {}), Charge = {}>'.\
        format(self.type, self.energy, self.x_coord, self.y_coord, self.z_coord, self.charge)

class MET: 
    """This holds information for the Missing Transverse Energy after each event"""
    # x_coord 
    # y_coord

    def __init__(self, px, py): 
        self.x_coord = px
        self.y_coord = py 

    def __repr__(self): 
        return u'<Missing transverse energy: Coordinates (X = {}, Y = {})>'.format(self.x_coord, self.y_coord) 
