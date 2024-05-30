// Bundled

import Foundation

// Class for holding parameters
class Parameters {
    var name: String // Default values not needed now!
    var height: Int
    var weight: Double

    init(_ filename: String) throws {

        // get_input
        let lines = try String(contentsOfFile: filename, encoding: String.Encoding.utf8)
            .components(separatedBy: "\n")
        
        self.name = lines[1]
        self.height = Int(lines[3]) ?? 0
        self.weight = Double(lines[5]) ?? 0
        
        // input_constraints
        if self.name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
            throw ParamError("Name must not be blank!")
        }
        else if self.height <= 0 {
            throw ParamError("Height must be positive!")
        }
        else if self.weight <= 0 {
            throw ParamError("Weight must be positive!")
        }
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

var p: Parameters = try Parameters("FileInputTests/input.txt")
print("Parameters(\"" + p.name + "\", " + String(p.height) + ", " + String(p.weight) + ")")