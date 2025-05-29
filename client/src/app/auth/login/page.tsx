'use client'

import { z } from 'zod'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { loginSchema } from '@/app/validations/validacao'
import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { BackgroundBeams } from '@/components/ui/background-beams'
import InputPadrao from '@/components/InputPadrao'
import { Button } from '@/components/ui/button'
import Link from 'next/link'

type LoginForm = z.infer<typeof loginSchema>

const Login = () => {
  const router = useRouter()
  const [mensagemErro, setMensagemErro] = useState(false)
  const [data, setData] = useState<LoginForm>()
  const { register, handleSubmit, formState: { errors }, reset, } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
  })

  const onSubmit = async (formData: LoginForm) => {
    setData(formData)
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/users/login/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: formData.username,
          password: formData.password
        })
      })

      if (!res.ok) {
        throw new Error(`Erro na requisição de login`)
      }
      router.push('/home')
      // const data = await res.json()
      // console.log(data.access) 

    } catch (error) {
      setMensagemErro(true)
      console.log("Deu erro: ", error)
    }
  }

  // const irPaginaCadastro = () => {
  //   router.push("/cadastro")
  // }

  return (
    <div className='bg-neutral-950 h-screen relative overflow-hidden flex justify-center flex-col'>
      <BackgroundBeams className="z-0" />
      <div className="w-full rounded-md relative flex flex-col items-center justify-center antialiased z-10">
        <div className="max-w-2xl mx-auto p-4">
          <h1 className="relative text-[50px] bg-clip-text text-white font-medium">
            Login
          </h1>
          <p className="text-neutral-400 max-w-lg mx-auto my-2 text-lg">
            Preencha os dados para entrar no Ordem e serviços do Senai.
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

            <label className='text-white mb-2'>Password</label>
            <input {...register("password")} type="password" className='bg-transparent border-1 border-gray-600 h-[35px] rounded text-white p-2' />
            {errors.password && <span className='text-red-500'>{errors.password.message}</span>}
          </div>
          <p className='text-red-500 pt-6 flex justify-center'>
            {mensagemErro ? 'Nome de usuário ou senha inválidos' : ''}
          </p>
          <div className="flex gap-10 flex-col">
            <Button type='submit' variant='outline' className='text-md h-10 cursor-pointer mt-6'>Entrar</Button>
            {/* <Button type='button' variant='ghost' className='h-10 text-gray-500 cursor-pointer hover:bg-[#181818] hover:text-white' onClick={() => reset()}>Limpar</Button> */}

            <Button variant='link' className='text-gray-500 cursor-pointer text-md'>
              <Link href='/register'>
                Ainda não tenho uma conta
              </Link>
            </Button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Login;