

def format_list_harvard(list_in):
    result = ''
    for i in range(len(list_in)):
        result += list_in[i]
        if(i < len(list_in) - 2):
            result += ', ' 
        elif(i == len(list_in) - 2):
            result += ' & ' 
    return result

class Paper:
    def __init__(self, title, authors, year, journal, volume_issue, pages, doi=None):
        self.title   = title
        self.year    = year
        self.authors = authors
        self.journal = journal
        self.vol_iss = volume_issue
        self.pages   = pages
        self.doi     = doi

    def print_harvard(self, indent=0):
        print(indent*' '+'<li>{} ({}), \'{}\', <i>{}</i>, {}, pp. {}</li>'.format(format_list_harvard(self.authors), self.year, self.title, self.journal, self.vol_iss, self.pages))

    def print_title_first(self, indent=0):
        if self.doi is None:
            print(indent*' '+'<li>{} ({}) {}, <i>{}</i>, {}, pp. {}</li>'.format(self.title, self.year, format_list_harvard(self.authors), self.journal, self.vol_iss, self.pages))
        else:
            print(indent*' '+'<li>{} ({}) {}, <i>{}</i>, {}, pp. {} (<a href=\"http://dx.doi.org/{}\">{}</a>)</li>'.format(self.title, self.year, format_list_harvard(self.authors), self.journal, self.vol_iss, self.pages, self.doi, self.doi))

cumulus = []

cumulus.append(Paper('Atmospheric Boundary Layer, Integrating Air Chemistry and Land Interactions', \
                    ['Vilà-Guerau De Arellano, J.', 'Heerwaarden, C.C. van', 'Stratum, B.J.H. van', 'Dries, C.L.A.M. van den'], \
                    2015, 'Cambridge University Press, New York', '', '265'))

cumulus.append(Paper('Study of a prototypical convective boundary layer observed during BLLAST: contributions by large-scale forcings', \
                    ['Pietersen, H.P.', 'Vilà-Guerau De Arellano, J.', 'Augustin, P.', 'Boer, A. van de', 'Coster, O. de', 'Delbarre, H.', 'Durand, P.', 'Fourmentin, M.', 'Gioli, B.', 'Hartogensis, O.K.', 'Lohou, F.', 'Lothon, M.', 'Ouwersloot, H.G.', 'Pino, D.', 'Reuder, J.'], \
                    2015, 'Atmospheric Chemistry and Physics', '15', '4241-4257', '10.5194/acp-15-4241-2015'))

cumulus.append(Paper('Subcloud-Layer Feedbacks Driven by the Mass Flux of Shallow Cumulus Convection over Land', \
                    ['Stratum, B.J.H. van', 'Vilà-Guerau De Arellano, J.', 'Heerwaarden, C.C. van', 'Ouwersloot, H.G.'], \
                    2015, 'Journal of the Atmospheric Sciences', '71', '881-895', '10.1175/JAS-D-13-0192.1'))

cumulus.append(Paper('Analytical solution for the convectively-mixed atmospheric boundary layer', \
                    ['Ouwersloot, H.G.', 'Vilà-Guerau de Arellano, J.'], \
                    2013, 'Boundary-Layer Meteorology', '148 (3)', '557-583', '10.1007/s10546-013-9816-z'))

cumulus.append(Paper('Quantifying the transport of subcloud layer reactants by shallow cimulus clouds over the Amazon', \
                    ['Ouwersloot, H.G.', 'Vilà-Guerau De Arellano, J.', 'Stratum, B.J.H. van', 'Krol, M.C.', 'Lelieveld, J.'], \
                    2013, 'Journal of Geophysical Research: Atmospheres', '118 (23)', '13,041-13,059', '10.1002/2013JD020431'))

cumulus.append(Paper('Modelled suppression of boundary-layer clouds by plants in a CO2-rich atmosphere', \
                    ['Vilà-Guerau de Arellano, J.', 'Heerwaarden, C.C. van', 'Lelieveld, J.'], \
                    2012, 'Nature geoscience', '5', '701-704', '10.1038/ngeo1554'))

cumulus.append(Paper('Boundary Layer Characteristics over Homogeneous and Heterogeneous Surfaces Simulated by MM5 and DALES', \
                    ['Braam, M.', 'Vilà-Guerau de Arellano, J.', 'Górska, M.'], \
                    2011, 'Journal of Applied Meteorology and Climatology', '50 (6)', '1372-1386', '10.1175/2011JAMC2552.1'))

cumulus.append(Paper('Understanding the daily cycle of evapotranspiration: a method to quantify the influence of forcings and feedbacks', \
                    ['Heerwaarden, C.C. van', 'Vilà-Guerau de Arellano, J.', 'Gounou, A.', 'Guichard, F.', 'Couvreux, F.'], \
                    2010, 'Journal of Hydrometeorology', '11 (6)', '1405-1422', '10.1175/2010JHM1272.1'))

cumulus.append(Paper('Land-atmosphere coupling explains the link between pan evaporation and actual evapotranspiration trends in a changing climate', \
                    ['Heerwaarden, C.C. van', 'Vilà-Guerau de Arellano, J.', 'Teuling, A.J.'], \
                    2010, 'Geophysical Research Letters', '37', 'L21401', '10.1029/2010GL045374'))

cumulus.append(Paper('Interactions between dry-air entrainment, surface evaporation and convective boundary-layer development', \
                    ['Heerwaarden, C.C. van', 'Vilà-Guerau de Arellano, J.', 'Moene, A.F.', 'Holtslag, A.A.M.'], \
                    2009, 'Quarterly Journal of the Royal Meteorological Society', '135 (642)', '1277-1291', '10.1002/qj.431'))

cumulus.append(Paper('Role of nocturnal turbulence and advection in the formation of shallow cumulus over land', \
                    ['Vilà-Guerau de Arellano, J.'], \
                    2007, 'Quarterly Journal of the Royal Meteorological Society', '133 (628)', '1615-1627', '10.1002/qj.138'))

cumulus.append(Paper('Representing Sheared Convective Boundary Layer by Zeroth- and First-Order-Jump Mixed-Layer Models: Large-Eddy Simulation Verification', \
                    ['Pino, D.', 'Vilà-Guerau de Arellano, J.', 'Kim, S.W.'], \
                    2006, 'Journal of Applied Meteorology and Climatology', '45 (9)', '1224-1243', '10.1175/JAM2396.1'))

cumulus.append(Paper('Parameterization of entrainment in a sheared convective boundary layer using a first-order jump model', \
                    ['Kim, S.W.', 'Park, S.U.', 'Pino, D.', 'Vilà-Guerau de Arellano, J.'], \
                    2006, 'Boundary-Layer Meteorology', '120 (3)', '455-475', '10.1007/s10546-006-9067-3'))

cumulus.append(Paper('Entrainment process of carbon dioxide in the atmospheric boundary layer', \
                    ['Vilà-Guerau de Arellano, J.', 'Gioli, B.', 'Miglietta F.', 'et al.'], \
                    2004, 'Journal of Geophysical Research', '109', 'D18110', '10.1029/2004JD004725'))

surface = []

surface.append(Paper('Two perspectives on the coupled carbon, water and energy exchange in the planetary boundary layer', \
                    ['Combe, M.', 'Vilà-Guerau De Arellano, J.', 'Ouwersloot, H.G.', 'Jacobs, C.M.J.', 'Peters, W.'], \
                    2015, 'Biogeosciences', '12', '103-123', '10.5194/bg-12-103-2015'))

surface.append(Paper('Understanding the impact of plant competition on the coupling between vegetation and the atmosphere', \
                    ['Loon, M.P. van', 'Dekker, S.C.', 'Anten, N.P.R.', 'Rietkerk, M.', 'Vilà-Guerau De Arellano, J.'], \
                    2015, 'Journal of Geophysical Research: Biogeosciences', '120', '2212-2228', '10.1002/2015JG003108'))

surface.append(Paper('Disentangling the response of forest and grassland energy exchange to heatwaves under idealized land-atmosphere coupling', \
                    ['Heerwaarden C.C. van', 'Teuling A.J.'], \
                    2014, 'Biogeosciences', '11', '6159-6171', '10.5194/bg-11-6159-2014'))

surface.append(Paper('Quantifying the uncertainties of advection and boundary layer dynamics on the diurnal carbon dioxide budget', \
                    ['Pino, D.', 'Kaikkonen, J.P.', 'Vilà-Guerau de Arellano, J.'], \
                    2013, 'Journal of Geophysical Research: Atmospheres', '118 (16)', '9376-9392', '10.1002/jgrd.50677'))

surface.append(Paper('A conceptual framework to quantify the influence of convective boundary layer development on carbon dioxide mixing ratios', \
                    ['Pino, D.', 'Vilà-Guerau de Arellano, J.', 'Peters, W.', 'Schröter, J.S.', 'Heerwaarden, C.C. van', 'Krol, M.C.'], \
                    2012, 'Atmospheric Chemistry and Physics', '122', '2969-2985', '10.5194/acp-12-2969-2012'))

surface.append(Paper('Diurnal and vertical variability of the sensible heat and carbon dioxide budgets in the atmospheric surface layer', \
                    ['Casso-Torralba, P.', 'Vilà-Guerau de Arellano, J.', 'Bosveld, F.', 'Soler, M.R.', 'Vermeulen, A.', 'Werner, C.', 'Moors, E.J.'], \
                    2008, 'Journal of Geophysical Research: Atmospheres', '113', 'D12119', '10.1029/2007JD009583'))

chemistry = []

chemistry.append(Paper('Cumulative ozone effect on canopy stomatal resistance and the impact on boundary layer dynamics and CO2 assimilation at the diurnal scale: A case study for grassland in the Netherlands', \
                      ['Super, I.', 'Vilà-Guerau De Arellano, J.', 'Krol, M.C.'], \
                      2015, 'Journal of Geophysical Research: Biogeosciences', '120', '1348-1365', '10.1002/2015JG002996'))

chemistry.append(Paper('Characterization of a boreal convective boundary layer and its impact on atmospheric chemistry during HUMPPA-COPEC-2010', \
                      ['Ouwersloot, H.G.', 'Vilà-Guerau de Arellano, J.', 'Nölscher, A.C.', 'Krol, M.C.', 'Ganzeveld, L.N.', 'Breitenberger, C.', 'Mammarella, I.', 'Williams, J.', 'Lelieveld, J.'], \
                      2012, 'Atmospheric Chemistry and Physics', '12', '9335-9353', '10.5194/acp-12-9335-2012'))

chemistry.append(Paper('Case study of the diurnal variability of chemically active species with respect to boundary layer dynamics during DOMINO', \
                      ['Stratum, B.J.H. van', 'Vilà-Guerau de Arellano, J.', 'Ouwersloot, H.G.', 'Dries, K. van den', 'Laar, T.W. van', 'Martinez, M.', 'Lelieveld, J.', 'Diesch, J.M.', 'Drewnick, F.', 'Fischer, H.', 'Hosaynali Beygi, Z.', 'Harder, H.', 'Regelin, E.', 'Sinha, V.', 'Adame, J.A.', 'Sörgel, M.', 'Sander, R.', 'Bozem, H.', 'Song, W.', 'Williams, J.', 'Yassaa, N.'], \
                      2012, 'Atmospheric Chemistry and Physics', '12', '5329 - 5341', '10.5194/acp-12-5329-2012'))

chemistry.append(Paper('The role of boundary layer dynamics on the diurnal evolution of isoprene and the hydroxyl radical over tropical forests', \
                      ['Vilà-Guerau de Arellano, J.', 'Patton, E.G.', 'Karl, T.', 'Dries, K. van den', 'Barth, M.C.', 'Orlando, J.J.'], \
                      2011, 'Journal of Geophysical Research: Atmospheres', '116', 'D07304', '10.1029/2010JD014857'))

chemistry.append(Paper('On inferring isoprene emission surface flux from atmospheric boundary layer concentration measurements', \
                      ['Vilà-Guerau de Arellano, J.', 'Dries, K. van den', 'Pino, D.'], \
                      2009, 'Atmospheric Chemistry and Physics', '9', '3629-3640', '10.5194/acp-9-3629-2009'))

chemistry.append(Paper('Introducing effective reaction rates to account for the inefficient mixing of the convective boundary layer', \
                      ['Vinuesa, J.F.', 'Vilà-Guerau de Arellano, J.'], \
                      2005, 'Atmospheric Environment', '39 (3)', '445-461', '10.1016/j.atmosenv.2004.10.003'))

aerosols = []

aerosols.append(Paper('Aerosols in the convective boundary layer: Shortwave radiation effects on the coupled land-atmosphere system', \
                     ['Wilde Barbaro, E.', 'Vilà-Guerau de Arellano, J.', 'Ouwersloot, H.G.', 'Schroter, J.S.', 'Donovan, D.P.', 'Krol, M.C.'], \
                     2014, 'Journal of Geophysical Research: Atmospheres', '119', '5845-5863', '10.1002/2013JD021237'))

aerosols.append(Paper('Influence of boundary layer dynamics and isoprene chemistry on the organic aerosol budget in a tropical forest', \
                     ['Janssen, R.H.H.', 'Vilà-Guerau de Arellano, J.', 'Jimenez, J.L.', 'Ganzeveld, L.N.', 'Robinson, N.H.', 'Allan, J.D.', 'Coe, H.', 'Pugh, T.A.M.'], \
                     2013, 'Journal of Geophysical Research: Atmospheres', '118 (16)', '9351–9366', '10.1002/jgrd.50672'))

aerosols.append(Paper('Impacts of Aerosol Shortwave Radiation Absorption on the Dynamics of an Idealized Convective Atmospheric Boundary Layer', \
                     ['Wilde Barbaro, E.', 'Vilà-Guerau de Arellano, J.', 'Krol, M.C.', 'Holtslag, A.A.M.'], \
                     2013, 'Boundary-Layer Meteorology', '148', '31-49', '10.1007/s10546-013-9800-7'))

aerosols.append(Paper('Combined effects of surface conditions, boundary layer dynamics and chemistry on diurnal SOA evolution', \
                     ['Janssen, R.H.H.', 'Vilà-Guerau de Arellano, J.', 'Ganzeveld, L.N.', 'Kabat, P.', 'Jimenez, J.L.', 'Farmer, D.K.', 'Heerwaarden, C.C. van', 'Mammarella, I.'], \
                     2012, 'Atmospheric Chemistry and Physics', '12 (15)', '6827-6843', '10.5194/acp-12-6827-2012'))


indent = 16
titles = ['Atmospheric boundary layer dynamics and clouds','Surface energy balance and CO2 budget','Chemistry','Aerosols' ]

for section,title in zip([cumulus, surface, chemistry, aerosols], titles):
    print(indent*' '+'<h4>{}</h4>'.format(title))
    print(indent*' '+'<ul>')
    for paper in section:
        #paper.print_harvard(indent+4)
        paper.print_title_first(indent+4)
    print(indent*' '+'</ul>')
    print(' ')
