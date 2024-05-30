// Unbundled

import Foundation

struct tempParameters {
    let name: String
    let height: Int
    let weight: Double
}

func get_input(_ filename: String) throws -> tempParameters {
    
    let lines = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
        .components(separatedBy: "\n")
    
    let name: String = lines[1]
    let height: Int = Int(lines[3]) ?? 0
    let weight: Double = Double(lines[5]) ?? 0

    return tempParameters(name:name, height:height, weight:weight)
}

func input_constraints(_ name: String,_ height: Int,_ weight: Double) throws -> Void {
    
    if name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
        throw ParamError("Name must not be blank!")
    }
    else if height <= 0 {
        throw ParamError("Height must be positive!")
    }
    else if weight <= 0 {
        throw ParamError("Weight must be positive!")
    }
}

// Simple error struct
struct ParamError: LocalizedError {
    let description: String

    init(_ description: String) {
        self.description = description
    }

    var errorDescription: String? {
        description
    }
}

let p: tempParameters
p = try get_input("FileInputTests/input.txt")

// This is a bit hacky again :(
let name: String, height: Int, weight: Double
name = p.name
height = p.height
weight = p.weight

try input_constraints(name, height, weight)
print(p)