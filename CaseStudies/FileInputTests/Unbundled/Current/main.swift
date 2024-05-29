// Unbundled

import Foundation

func get_input(_ filename: String) throws -> (String, Int, Double) {
    
    let lines = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
        .components(separatedBy: "\n")
    
    let name: String = lines[1]
    let height: Int = Int(lines[3]) ?? 0
    let weight: Double = Double(lines[5]) ?? 0

    return (name, height, weight)
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

let name: String, height: Int, weight: Double
(name, height, weight) = try get_input("FileInputTests/input.txt")
try input_constraints(name, height, weight)
print((name, height, weight))