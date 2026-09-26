#My first simple simulation
from rocketpy import Environment , SolidMotor , Rocket , Flight
import datetime

environment = Environment(latitude=32.990254,longitude=-106.974998,elevation=1400)

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

#Esto esta en UTC 
environment.set_date((tomorrow.year , tomorrow.month,tomorrow.day,12))

environment.set_atmospheric_model(type="Forecast",file="GFS")

# Para printear toda la informacion de las condiciones del enviroment
# environment.info()   ## parece que todos los objetos de la libreria de rocketpy tienen la funcion info()

# Definir el motor 
Pro75M1670 = SolidMotor(
    thrust_source="data/motors/cesaroni/Cesaroni_M1670.eng",
    dry_mass=1.815,
    dry_inertia=(0.125, 0.125, 0.002),
    nozzle_radius=33 / 1000,
    grain_number=5,
    grain_density=1815,
    grain_outer_radius=33 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height=120 / 1000,
    grain_separation=5 / 1000,
    grains_center_of_mass_position=0.397,
    center_of_dry_mass_position=0.317,
    nozzle_position=0,
    burn_time=3.9,
    throat_radius=11 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)
# Nota importante
"""(parameter) dry_inertia: tuple[float, float, float]
dry_inertia : tuple, list
Tuple or list containing the motor's dry mass inertia tensor components, in kg*m^2. 
This inertia is defined with respect to the the center_of_dry_mass_position position. Assuming e_3 is the rocket's axis of symmetry, e_1 and e_2 are orthogonal and form a plane perpendicular to e_3, 
the dry mass inertia tensor components must be given in the following order: (I_11, I_22, I_33, I_12, I_13, I_23),
where I_ij is the component of the inertia tensor in the direction of e_i x e_j. Alternatively, the inertia tensor can be given as (I_11, I_22, I_33), where I_12 = I_13 = I_23 = 0."""

simpleRocket = Rocket(
    radius = 127/2000 , 
    mass = 14.426 , 
    inertia=(6.321, 6.321, 0.034),
    power_off_drag="data/rockets/calisto/powerOffDragCurve.csv",
    power_on_drag="data/rockets/calisto/powerOnDragCurve.csv",
    center_of_mass_without_motor=0,
    coordinate_system_orientation="tail_to_nose",
)

simpleRocket.add_motor(Pro75M1670,position=-1.255)

rail_buttons = simpleRocket.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
)

nose_cone = simpleRocket.add_nose(
    length=0.55829, kind="von karman", position=1.278
)

fin_set = simpleRocket.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("data/airfoils/NACA0012-radians.txt","radians"),
)

tail = simpleRocket.add_tail(
    top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
)

main = simpleRocket.add_parachute(
    name="main",
    cd_s=10.0,
    trigger=800,      # ejection altitude in meters
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
    radius=1.5,
    height=1.5,
    porosity=0.0432,
)

drogue = simpleRocket.add_parachute(
    name="drogue",
    cd_s=1.0,
    trigger="apogee",  # ejection at apogee
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
    radius=1.5,
    height=1.5,
    porosity=0.0432,
)

# simpleRocket.plots.static_margin() 
# simpleRocket.draw()

test_flight = Flight(
    rocket=simpleRocket, environment=environment , rail_length=5.2 , inclination=85 , heading=0)

test_flight.info()
test_flight.plots.trajectory_3d()