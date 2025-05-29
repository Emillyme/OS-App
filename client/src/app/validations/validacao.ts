import { z } from "zod"; 

export const loginSchema = z.object({
    username: z.string()
        .nonempty("Digite seu username")
        .regex(/^[A-Za-z]+$/i, "Apenas letras são permitidas!"),
    password: z.string()
        .nonempty("Digite sua senha")
})

export const signupSchema = z.object({
    username: z.string()
        .nonempty("Digite um username"),
    email: z.string()
        .nonempty("Digite um email")
        .regex(/^[\w.-]+@gmail\.com$/, "Apenas emails Gmail é permitido"),
    password: z.string()
        .nonempty("Digite uma senha"),
})
