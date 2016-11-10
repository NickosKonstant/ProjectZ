namespace Freecon
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    public partial class MemberService
    {
        public int Id { get; set; }

        [StringLength(128)]
        public string MemberID { get; set; }

        public int? ServiceID { get; set; }

        public int? ServiceCostPerHour { get; set; }

        public virtual Member Member { get; set; }
    }
}
