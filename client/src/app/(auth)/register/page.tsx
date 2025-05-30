'use client'

import { loginSchema, signupSchema } from "@/app/validations/validacao";
import { BackgroundBeams } from "@/components/ui/background-beams";
import { Button } from "@/components/ui/button";
import { zodResolver } from "@hookform/resolvers/zod";
import Link from "next/link";
import { useRouter } from 'next/navigation'
import { useState } from "react";
import { useForm } from "react-hook-form";
import { z } from "zod";

type SignupForm = z.infer<typeof signupSchema>

const register = () => {
    const router = useRouter()
    const [mensagemErro, setMensagemErro] = useState(false)
    const [data, setData] = useState<SignupForm>()
    const { register, handleSubmit, formState: { errors }, reset, } = useForm<SignupForm>({
        resolver: zodResolver(signupSchema),
    })

    const onSubmit = async (formData: SignupForm) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/users/signup/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: formData.username,
                    email: formData.email,
                    password: formData.password
                })
            })

            if (!response.ok) {
                throw new Error('Erro na requisição de signup de usuário comum')
            }
            console.log('Cadastrado')
            router.push('/login')
        } catch (error) {
            console.log("Deu erro: ", error)
        }
    }
    
    return (
        <>
            <div className='bg-neutral-950 h-screen relative overflow-hidden flex justify-center flex-col'>
                <BackgroundBeams className="z-0" />
                <div className="w-full rounded-md relative flex flex-col items-center justify-center antialiased z-10">
                    <div className="max-w-2xl mx-auto p-4">
                        <h1 className="relative text-[50px] bg-clip-text text-white font-medium">
                            Sign up
                        </h1>
                        <p className="text-neutral-400 max-w-lg mx-auto my-2 text-lg">
                            Preencha os dados para seu cadastro no Ordem e Serviços do Senai.
                        </p>
                    </div>
                </div>

                <div className="flex justify-center items-center z-10 relative mt-10">
                    <form onSubmit={handleSubmit(onSubmit)}>
                        <div className="flex flex-col w-120">
                            <label className='text-white mb-2'>Username</label>
                            <input {...register("username")} type="text" className='bg-transparent border-1 border-gray-600 h-[35px] rounded text-white p-2' />
                            {errors.username && <span className="text-red-500">{errors.username.message}</span>}
                            <span className='h-7'></span>

                            <label className='text-white mb-2'>Email</label>
                            <input {...register("email")} type="text" className='bg-transparent border-1 border-gray-600 h-[35px] rounded text-white p-2' />
                            {errors.email && <span className="text-red-500">{errors.email.message}</span>}
                            <span className='h-7'></span>

                            <label className='text-white mb-2'>Password</label>
                            <input {...register("password")} type="password" className='bg-transparent border-1 border-gray-600 h-[35px] rounded text-white p-2' />
                            {errors.password && <span className='text-red-500'>{errors.password.message}</span>}
                            <span className='h-7'></span>

                            <label className='text-white mb-2'>Confirm password</label>
                            <input {...register("confirm")} type="password" className='bg-transparent border-1 border-gray-600 h-[35px] rounded text-white p-2' />
                            {errors.confirm && <span className='text-red-500'>{errors.confirm.message}</span>}
                        </div>
                        <p className='text-red-500 pt-6 flex justify-center'>
                            {mensagemErro ? 'Nome de usuário ou senha inválidos' : ''}
                        </p>
                        <div className="flex gap-10 flex-col">
                            <Button type='submit' variant='outline' className='text-md h-10 cursor-pointer mt-6'>Cadastrar</Button>
                            {/* <Button type='button' variant='ghost' className='h-10 text-gray-500 cursor-pointer hover:bg-[#181818] hover:text-white' onClick={() => reset()}>Limpar</Button> */}

                            <Button variant='link' className='text-gray-500 cursor-pointer text-md'>
                                <Link href='/login'>
                                    Já tenho uma conta
                                </Link>
                            </Button>
                        </div>
                    </form>
                </div>
            </div>
        </>
    );
}

export default register;