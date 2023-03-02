<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-log4j12</artifactId>
  <version>1.7.30</version>
</dependency>

2.	Configure log4j2 to use MDC in your log4j2.xml file:

<Configuration>
  <Properties>
    <Property name="pattern">%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{36} [%X{correlationId}, %X{uniqueId}] - %msg%n</Property>
  </Properties>
  <Appenders>
    <Console name="Console" target="SYSTEM_OUT">
      <PatternLayout pattern="${pattern}"/>
    </Console>
    <File name="File" fileName="logs/app.log">
      <PatternLayout pattern="${pattern}"/>
    </File>
  </Appenders>
  <Loggers>
    <Root level="info">
      <AppenderRef ref="Console"/>
      <AppenderRef ref="File"/>
    </Root>
  </Loggers>
</Configuration>

3.	Define your MDC keys and add them to your log messages:

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

public class MyService {
  private static final Logger LOGGER = LoggerFactory.getLogger(MyService.class);
  private static final String CORRELATION_ID_KEY = "correlationId";
  private static final String UNIQUE_ID_KEY = "uniqueId";
  
  public void doSomething() {
    String correlationId = generateCorrelationId();
    String uniqueId = generateUniqueId();
    MDC.put(CORRELATION_ID_KEY, correlationId);
    MDC.put(UNIQUE_ID_KEY, uniqueId);
    LOGGER.info("Doing something...");
    MDC.remove(CORRELATION_ID_KEY);
    MDC.remove(UNIQUE_ID_KEY);
  }
  
  private String generateCorrelationId() {
    // generate a unique correlation ID
  }
  
  private String generateUniqueId() {
    // generate a unique ID
  }
}

4.	Use AspectJ to add the MDC keys to your logs:

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.slf4j.MDC;

@Aspect
public class LoggingAspect {
  private static final String CORRELATION_ID_KEY = "correlationId";
  private static final String UNIQUE_ID_KEY = "uniqueId";
  
  @Before("execution(* com.example..*(..))")
  public void before(JoinPoint joinPoint) {
    String correlationId = MDC.get(CORRELATION_ID_KEY);
    if (correlationId == null) {
      correlationId = generateCorrelationId();
      MDC.put(CORRELATION_ID_KEY, correlationId);
    }
    
    String uniqueId = MDC.get(UNIQUE_ID_KEY);
    if (uniqueId == null) {
      uniqueId = generateUniqueId();
      MDC.put(UNIQUE_ID_KEY, uniqueId);
    }
  }
  
  private String generateCorrelationId() {
    // generate a unique correlation ID
  }
  
  private String generateUniqueId() {
    // generate a unique ID
  }
}


logback.xml

<configuration>

  <!-- Define the MDC values you want to log -->
  <property name="mdcValues" value="correlationId,uniqueId"/>

  <!-- Define the pattern layout that includes the MDC values -->
  <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{ISO8601} [%thread] %-5level %logger{36} [%property{correlationId}] [%property{uniqueId}] - %msg%n</pattern>
    </encoder>
  </appender>

  <!-- Set up the MDC filter -->
  <filter class="ch.qos.logback.classic.filter.MDCFilter">
    <key>correlationId</key>
    <value>.*</value>
  </filter>
  <filter class="ch.qos.logback.classic.filter.MDCFilter">
    <key>uniqueId</key>
    <value>.*</value>
  </filter>

  <!-- Attach the filter to the appropriate logger -->
  <logger name="com.example" level="DEBUG">
    <appender-ref ref="console"/>
    <filter ref="correlationId"/>
    <filter ref="uniqueId"/>
  </logger>

</configuration>

Aspect class

