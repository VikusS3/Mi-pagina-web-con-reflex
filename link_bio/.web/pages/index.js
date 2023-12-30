
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Avatar, Box, Button, Center, Flex, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <HStack sx={{"position": "sticky", "bg": "#17161B", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0"}}>
  <Box sx={{"fontSize": "1.5em", "fontFamily": "Comfortaa-Medium"}}>
  <Text as={`span`} sx={{"color": "#950101", "fontFamily": "Comfortaa-Medium"}}>
  {`saul`}
</Text>
  <Text as={`span`} sx={{"color": "#B01212", "fontFamily": "Comfortaa-Medium"}}>
  {`dev`}
</Text>
</Box>
</HStack>
  <Center>
  <VStack sx={{"maxWidth": "600px", "width": "100%", "marginY": "2em", "padding": "2em"}}>
  <VStack alignItems={`start`} spacing={`2em`}>
  <HStack spacing={`2em`}>
  <Avatar name={`VikusS3 dev`} size={`xl`} src={`avatar.jpg`} sx={{"color": "#17161B", "bg": "#950101", "padding": "2px", "boder": "5px", "boderColor": "#950101"}}/>
  <VStack alignItems={`start`}>
  <Heading size={`lg`} sx={{"color": "#F1F2F4"}}>
  {`saul orellana`}
</Heading>
  <Text sx={{"maringTop": ["0px !important"], "color": "#C3C7CB"}}>
  {`@vikusss3dev`}
</Text>
  <HStack spacing={`2em`}>
  <Link as={NextLink} href={`https://github.com/VikusS3`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage src={`icons/github.svg`} sx={{"width": "2em"}}/>
</Link>
  <Link as={NextLink} href={`https://github.com/SaulFOC`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage src={`icons/github-alt.svg`} sx={{"width": "2em"}}/>
</Link>
  <Link as={NextLink} href={`https://facebook.com/profile.php?id=61554249853628&locale=es_LA`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage src={`icons/facebook.svg`} sx={{"width": "2em"}}/>
</Link>
</HStack>
</VStack>
</HStack>
  <Flex sx={{"width": "100%"}}>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#950101"}}>
  {`Edad:`}
</Text>
  {` 21 años`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#950101"}}>
  {`Ciudad:`}
</Text>
  {` Lima, Perú`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#950101"}}>
  {`Email:`}
</Text>
  {` felix21soc@gmail.com`}
</Box>
</Flex>
  <Text sx={{"fontSize": "1em", "color": "#C3C7CB"}}>
  {`Soy tecnico en sistemas y programador con mas de un año de experiencia.
                Actualmente trabajo como freelance full-stack developer python, php y ASP.NET.
                Ademos de ser un apasionado por la tecnologia, me gusta mucho la musica y los 
                videojuegos.`}
</Text>
</VStack>
  <VStack spacing={`1em`} sx={{"width": "100%"}}>
  <Heading size={`lg`} sx={{"width": "100%", "fontFamily": "Comfortaa-Regular", "paddingTop": "1em", "color": "#F1F2F4"}}>
  {`Mis Redes Sociales`}
</Heading>
  <Link as={NextLink} href={`https://www.twitch.tv/vikussss3`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "boderRadius": "0.5em", "color": "#C3C7CB", "backgroundColor": "#28272C", "_hover": {"backgroundColor": "#950101", "color": "#F1F2F4"}}}>
  <HStack>
  <ChakraImage src={`icons/twitch.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": ["0px !important"]}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Comfortaa-Regular", "color": "#F1F2F4"}}>
  {`Twitch`}
</Text>
  <Text sx={{"fontSize": "0.8em", "fontFamily": "Arial, Helvetica, sans-serif", "Color": "#C3C7CB"}}>
  {`Directos de vez en cuando`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.youtube.com/channel/UCWTqiQVIA08vVTJhwy1SaDQ`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "boderRadius": "0.5em", "color": "#C3C7CB", "backgroundColor": "#28272C", "_hover": {"backgroundColor": "#950101", "color": "#F1F2F4"}}}>
  <HStack>
  <ChakraImage src={`icons/youtube.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": ["0px !important"]}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Comfortaa-Regular", "color": "#F1F2F4"}}>
  {`Youtube`}
</Text>
  <Text sx={{"fontSize": "0.8em", "fontFamily": "Arial, Helvetica, sans-serif", "Color": "#C3C7CB"}}>
  {`Guias y Tutoriales`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "boderRadius": "0.5em", "color": "#C3C7CB", "backgroundColor": "#28272C", "_hover": {"backgroundColor": "#950101", "color": "#F1F2F4"}}}>
  <HStack>
  <ChakraImage src={`icons/linkedin.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": ["0px !important"]}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Comfortaa-Regular", "color": "#F1F2F4"}}>
  {`Linkedin`}
</Text>
  <Text sx={{"fontSize": "0.8em", "fontFamily": "Arial, Helvetica, sans-serif", "Color": "#C3C7CB"}}>
  {`Informacion profesional`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://twitter.com/Vikus3S`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "boderRadius": "0.5em", "color": "#C3C7CB", "backgroundColor": "#28272C", "_hover": {"backgroundColor": "#950101", "color": "#F1F2F4"}}}>
  <HStack>
  <ChakraImage src={`icons/x-twitter.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": ["0px !important"]}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Comfortaa-Regular", "color": "#F1F2F4"}}>
  {`Twitter`}
</Text>
  <Text sx={{"fontSize": "0.8em", "fontFamily": "Arial, Helvetica, sans-serif", "Color": "#C3C7CB"}}>
  {`Actualizacion de estados y publicaciones`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Heading size={`lg`} sx={{"width": "100%", "fontFamily": "Comfortaa-Regular", "paddingTop": "1em", "color": "#F1F2F4"}}>
  {`Contacto`}
</Heading>
  <Link as={NextLink} href={`mailto:felix21soc@gmail.com`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "boderRadius": "0.5em", "color": "#C3C7CB", "backgroundColor": "#28272C", "_hover": {"backgroundColor": "#950101", "color": "#F1F2F4"}}}>
  <HStack>
  <ChakraImage src={`icons/envelope-solid.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": ["0px !important"]}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Comfortaa-Regular", "color": "#F1F2F4"}}>
  {`Email`}
</Text>
  <Text sx={{"fontSize": "0.8em", "fontFamily": "Arial, Helvetica, sans-serif", "Color": "#C3C7CB"}}>
  {`¿Quieres colaborar conmigo?`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`mailto:felix.orellanac@istpargentina.edu.pe`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "display": "block", "padding": "0.5em", "boderRadius": "0.5em", "color": "#C3C7CB", "backgroundColor": "#28272C", "_hover": {"backgroundColor": "#950101", "color": "#F1F2F4"}}}>
  <HStack>
  <ChakraImage src={`icons/school-solid.svg`} sx={{"width": "2em", "height": "2em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"margin": ["0px !important"]}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Comfortaa-Regular", "color": "#F1F2F4"}}>
  {`MyEmailEducation`}
</Text>
  <Text sx={{"fontSize": "0.8em", "fontFamily": "Arial, Helvetica, sans-serif", "Color": "#C3C7CB"}}>
  {`felix.orellanac@istpargentina.edu.pe`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
</VStack>
</VStack>
</Center>
  <VStack sx={{"marginBottom": "2em", "paddingBottom": "2em", "color": "#A3ABB2"}}>
  <ChakraImage src={`logo.png`}/>
  <Link as={NextLink} href={`https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/`} isExternal={true} sx={{"fontSize": "0.8em", "textDecoration": "none", "_hover": {}}}>
  {`© 2021-2023 VikusS3dev V1 By Saul Orellana`}
</Link>
  <Text sx={{"fontSize": "0.8em", "maringTop": ["0px !important"]}}>
  {`Building with Reflex and Python`}
</Text>
</VStack>
</Box>
  <NextHead>
  <title>
  {`SaulDev | aprendiendo a programar dia a dia`}
</title>
  <meta content={`Hola mi nombre es Saul Orellana, soy un desarrollador full-stack junior, me gusta aprender cosas nuevas y compartir lo que aprendo, en este blog encontraras tutoriales de programacion, desarrollo web, desarrollo movil, desarrollo de videojuegos, y mucho mas, espero que te guste.`} name={`description`}/>
  <meta content={`avatar.jpg`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
