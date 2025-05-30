import { z } from "zod"; 

export const loginSchema = z.object({
    username: z.string()
        .nonempty("Digite seu username"),
    password: z.string().min(5)
        .nonempty("Digite sua senha")
})

export const signupSchema = z.object({
    username: z.string()
        .nonempty("Digite um username")
        .regex(/^[A-Za-z]+$/i, "Apenas letras são permitidas!"),
    email: z.string()
        .nonempty("Digite um email")
        .regex(/^[\w.-]+@gmail\.com$/, "Apenas emails Gmail é permitido"),
    password: z.string().min(5)
        .nonempty("Digite uma senha"),
    confirm: z.string().min(5)
}).refine((data) => data.username === data.confirm, {
    message: "Senhas não batem",
    path: ["confirm"],
})
