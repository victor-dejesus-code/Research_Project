from rocketpy import Environment, SolidMotor, Flight, Rocket
from rocketpy.simulation import FlightDataExporter  # for export simulations results
from pathlib import Path

# Aeropuerto Eugenio Maria de Hostos , mayaguez
enviroment = Environment(
    latitude = 18.255686 ,
    longitude=-67.148472,
    elevation= 8.75 ,
    timezone= "America/Puerto_Rico"
    
)
enviroment.set_atmospheric_model(type="custom_atmosphere", wind_v=-5)

# Defining the solid motor that will be used
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
# Defining first Rocket
r1 = Rocket(
    radius= 127/2000,
    mass= 14.426,
    inertia=(6.321, 6.321, 0.034), # same inertia as the documentation example
    power_off_drag="data/rockets/calisto/powerOffDragCurve.csv",
    power_on_drag="data/rockets/calisto/powerOnDragCurve.csv",
    center_of_mass_without_motor=0,
    coordinate_system_orientation="tail_to_nose"

)
r1.add_motor(Pro75M1670,position=-1.255)
ail_buttons = r1.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
)

nose_cone = r1.add_nose(
    length=0.55829, kind="von karman", position=1.278
)

fin_set = r1.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("data/airfoils/NACA0012-radians.txt","radians"),
)

tail = r1.add_tail(
    top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
)

main = r1.add_parachute(
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

drogue = r1.add_parachute(
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

# Defining second Rocket
r2 = Rocket(
    radius= 127/2000,
    mass= 14.426,
    inertia=(7.321,7.321,0.034), # new inertia incremented 1.000 kg*m^2
    power_off_drag="data/rockets/calisto/powerOffDragCurve.csv",
    power_on_drag="data/rockets/calisto/powerOnDragCurve.csv",
    center_of_mass_without_motor=0,
    coordinate_system_orientation="tail_to_nose"
)

r2.add_motor(Pro75M1670,position=-1.255)
ail_buttons = r2.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
)

nose_cone = r2.add_nose(
    length=0.55829, kind="von karman", position=1.278
)

fin_set = r2.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("data/airfoils/NACA0012-radians.txt","radians"),
)

tail = r2.add_tail(
    top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
)

main = r2.add_parachute(
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

drogue = r2.add_parachute(
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

# Flights
Flight1 = Flight(
    rocket=r1,
    environment= enviroment,
    rail_length=5.2,
    inclination= 90,
    heading=0,
    max_time_step=0.01,
    max_time=5
 )

Flight2 = Flight(
    rocket=r2,
    environment= enviroment,
    rail_length=5.2,
    inclination= 90,
    heading=0,
    max_time_step=0.01,
    max_time=5
 )

results_directory = Path("simulations/results")

variables = (
    "altitude",
    "speed",
    "acceleration",
    "mach_number",
    "angle_of_attack",
    "dynamic_pressure",
    "stability_margin",
)

#FlightDataExporter(Flight1).export_data(str(results_directory / "flight1.csv"),*variables,time_step=0.01)

#FlightDataExporter(Flight2).export_data(str(results_directory / "flight2.csv"),*variables,time_step=0.01)
