# Bundled

# Struct for holding parameters.
struct Parameters
    name::AbstractString
    height::Integer
    weight::AbstractFloat

    # This needs to be an inner constructor now, as it has
    # the same type signature as the struct itself.
    function Parameters(name::AbstractString, height::Integer, weight::AbstractFloat)
    
        parameters = new(name, height, weight)
        input_constraints(parameters) # This needs to be specified as "after initialization" or something
        return parameters
    end
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

# No longer part of the Parameters 'class'
function get_input(filename::AbstractString)

    file = open(filename, "r")
    lines = readlines(file)
    close(file)

    name = lines[2]
    height = parse(Int32, lines[4])
    weight = parse(Float64, lines[6])

    return Parameters(name, height, weight)
end

p = get_input("FileInputTests/input.txt")
println(p)