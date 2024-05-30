# Bundled

# Struct for holding parameters.
struct Parameters
    name::AbstractString
    height::Integer
    weight::AbstractFloat
end

function Parameters(filename::AbstractString)
    
    # We have to know that get_input has values for our parameters.  We can do 
    # this by explicitly telling GOOL this (Design 4) or by making it a function
    # (not a method) in GOOL itself (Design 6)
    params = get_input(filename)
    parameters = Parameters(params["name"], params["height"], params["weight"])
    # We have to know that we need to call this after the struct has been
    # instantiated.  We could do this by assuming that all `this` method calls
    # within the constructor are to stuff like validators, which can be safely 
    # called after creating the instance; or we could have an extra field for
    # stuff like this.
    input_constraints(parameters)
    return parameters
end

function get_input(filename::AbstractString)

    file = open(filename, "r")
    lines = readlines(file)
    close(file)

    name = lines[2]
    height = parse(Int32, lines[4])
    weight = parse(Float64, lines[6])

    return Dict(
        "name" => name,
        "height" => height,
        "weight" => weight
    )
end

function input_constraints(p::Parameters)

    if isempty(strip(p.name))
        throw("Name must not be blank!")
    elseif p.height <= 0
        throw("Height must be positive!")
    elseif p.weight <= 0
        throw("Weight must be positive!")
    end
end

p = Parameters("FileInputTests/input.txt")
println(p)