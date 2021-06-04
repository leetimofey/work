model lab5
Real beta=1, nu=0.3;
Real s(start=0.999), i(start=0.001), r(start=0);
equation
der(s)=-beta*s*i;
der(i)=beta*s*i-nu*i;
der(r)=nu*i;
end lab5;
