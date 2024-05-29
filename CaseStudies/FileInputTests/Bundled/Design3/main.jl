# Bundled

#=
    This does seem like the 'right way' to do it for a procedural language.
    It feels off for OO though - validation should be kept within the class.
=#

# Struct for holding parameters.
struct Parameters
    name::AbstractString
    height::Integer
    weight::AbstractFloat
end

# We don't even need a constructor, so that simplifies things a lot

# No longer part of the Parameters 'class'
# Validation is done inside here now
function get_input(filename::AbstractString)

    file = open(filename, "r")
    lines = readlines(file)
    close(file)

    name = lines[2]
    if isempty(strip(name))
        throw("Name must not be blank!")
    end
    height = parse(Int32, lines[4])
    if height <= 0
        throw("Height must be positive!")
    end
    weight = parse(Float64, lines[6])
    if weight <= 0
        throw("Weight must be positive!")
    end

    return Parameters(name, height, weight)
end

p = get_input("FileInputTests/input.txt")
println(p)