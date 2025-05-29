interface InputProps {
  typeInput: string
}

const InputPadrao = ({ typeInput }: InputProps) => {
    return(
       <input type={typeInput} className='bg-transparent border-1 border-gray-600 h-[35px] rounded text-white' /> 
    );
}

export default InputPadrao
