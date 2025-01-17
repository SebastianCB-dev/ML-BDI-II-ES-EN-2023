import { LoggerService as Logger } from '../classes'
import { ENV_VARIABLES, ENV_VALUES_RUNTIME, NODE_ENV_VALUES } from '../constants/env'

export const validateEnv = (): boolean => {
  let existsEnv: boolean = true
  const logger: Logger = new Logger()

  ENV_VARIABLES.forEach((env: string) => {
    if (process.env[env] === undefined || process.env[env]?.length === 0) {
      logger.infoLog(`ℹ️ Environment variable '${env}' is not properly set`)
      existsEnv = false
    }
    if (env === NODE_ENV_VALUES.ENVIRONMENT && (!ENV_VALUES_RUNTIME.includes(process.env[env] ?? ''))) {
      logger.infoLog(`ℹ️ Environment variable '${env}' is not a valid value, please use one of the following values: ${ENV_VALUES_RUNTIME.join(', ')}`)
      existsEnv = false
    }
  })
  return existsEnv
}
